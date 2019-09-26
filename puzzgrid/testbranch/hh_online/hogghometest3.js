'use strict'

let log = console.log.bind(console),
  id = val => document.getElementById(val),
  ul = id('ul'),
  gUMbtn = id('gUMbtn'),
  start = id('start'),
  stop = id('stop'),
  recordingCB = id('recording_cb'),
  stream,
  recorder,
  counter=1,
  chunks,
  media;


gUMbtn.onclick = e => {
  let mv = id('mediaAudio'),
      mediaOptions = {
        audio: {
          tag: 'audio',
          type: 'audio/wav', //ogg, wav also works
          ext: '.wav', //ogg
          gUM: {audio: true}
        }
      };
  media = mediaOptions.audio;
  navigator.mediaDevices.getUserMedia(media.gUM).then(_stream => {
    stream = _stream;
    id('gUMArea').style.display = 'none';
    id('btns').style.display = 'inherit';
    start.removeAttribute('disabled');
    recorder = new MediaRecorder(stream);
    recorder.ondataavailable = e => {
      chunks.push(e.data);
      if(recorder.state == 'inactive')  makeLink();
    };
    log('got media successfully');
  }).catch(log);
}

// start.onclick = e => {
  // start.disabled = true;
  // stop.removeAttribute('disabled');
  // chunks=[];
  // recorder.start();
// }


// stop.onclick = e => {
  // stop.disabled = true;
  // recorder.stop();
  // start.removeAttribute('disabled');
// }

recordingCB.onclick = e => {
	if(document.getElementById("recording_cb").checked == true){
		console.log("on");
		//start.disabled = true;
		//stop.removeAttribute('disabled');
		chunks=[];
		recorder.start();
	}
	else {
		console.log("off");
		//stop.disabled = true;
		recorder.stop();
		//console.log(chunks); //this logs an empty array, so maybe not?
		//####***                  Looks like chunks is the var where the audio stream is
		//start.removeAttribute('disabled');
	}
	
}



function makeLink(){ //blob converts chunks (audio stream) to blob format, which can be downloaded
  let blob = new Blob(chunks, {type: media.type })
    , url = URL.createObjectURL(blob) //creates a url to blob
    , li = document.createElement('li') //makes a div box thing
    , mt = document.createElement(media.tag) //is the media playback thing
    , hf = document.createElement('a') //this is to be the download link, the a being a link click thing
  ;
  console.log(url); 
  console.log(blob)//this works, so can I post the blob?
  mt.controls = true; //allows controls
  mt.src = url; //means thaT the playbackthing plays blob
  hf.href = url;  //adds the download links src as the blob--- This is the part at where the audio can be downloaded
  hf.download = `${counter++}${media.ext}`; //`` is php, sets the file name and type (ogg)
  hf.innerHTML = `donwload ${hf.download}`; //ammends the html to say 'download', then the file name
  li.appendChild(mt);  //this puts mt and hf into the box which is li
  li.appendChild(hf);
  ul.appendChild(li);
  
  
  //i think that to post with js, make the upload html box hidden, and use js to change to submit button value to true
  var audio_url = url;
  var audio_url_str = JSON.stringify(audio_url);
  $.ajax({
    url: 'audio_recv.php',
    type: 'POST',
    data: {audio_url: audio_url_str},
    success: function(response){
        console.log("Sucsessfull post");
		}
	});

}
