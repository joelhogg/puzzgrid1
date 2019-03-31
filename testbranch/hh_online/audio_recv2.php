<?php
$targetdir = "audio_catcher/";
$goodupload = 1;
$postedfile = $targetdir . basename($_FILES["audiofile"]["name"]);

$filetype = $_FILES['audiofile']['type'];
$extensions= array("audio/mp3","audio/wav","audio/ogg");

if(in_array($filetype,$extensions)=== false){
         echo "extension not allowed, valid extentions are: mp3, ogg, wav.";
		 $goodupload = 0;
      }
	  
$filesize = $_FILES['audiofile']['size'];

if ($filesize > 5000000) {
	echo "file too large, files cannot be bigger than 5MB.";
	$goodupload = 0;
}





if ($goodupload == 1){
	if (move_uploaded_file($_FILES["audiofile"]["tmp_name"], $postedfile)) {
        echo "The file ". basename( $_FILES["audiofile"]["name"]). " has been uploaded.";
    }
	else { echo "Sorry, there was an error uploading your file."; }
	echo "file has been uploaded!";
}

header ("Location: index.html");
?>