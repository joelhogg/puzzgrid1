<html>
<body id="body1">
	<title>hmm...Is Joe Awake?</title>
	<div id="header">
	<head>Is Joe Steer Awake?
		<link rel="icon" type="image/x-icon" href="favicon.ico" />
	</head>
	</div>
	<h1 id="printoutsleepstatus">null</h1>
	
	<link rel="stylesheet" href="style.css" type="text/css" media="screen" />
	
	<?php
		$sleepstatus = file("sleepstatusfile.txt");
		$sleepstatus = $sleepstatus[0];
		$sleepstatus = trim($sleepstatus);
	?>
	<script>
		translatestatus = '<?php echo $sleepstatus; ?>'
		if (translatestatus == "awake"){
		document.getElementById("printoutsleepstatus").innerHTML="Joe Steer is Awake!";
		}
		else if (translatestatus == "asleep"){
			document.getElementById("printoutsleepstatus").innerHTML="Joe Steer is Asleep :(";
		}
	</script>
	
	<form action="takepost.php" method="post" id="form">
		<br> <br>
		Admin Login: <input type="password" name="adminpassword"/>
		<br> <br>
		Choice: <select name="sleepstatuschoice" type="text">
					<option>Select a Status...</option>
					<option value="awake">Awake</option>
					<option value="asleep">Alseep</option>
				</select>
		<br> <br>
		Submit update: <input type="submit" value="Login">
	</form>
	
	
	<form action="upload.php" method="post" enctype="multipart/form-data">
		<hr> <br>
		Upload a more recent image:
		<input type="file" name="filetoupload" id="filetoupload"/>
		<input type="submit" value="Upload!" name="submit" />
		
	</form>

</body>
<div class=joepic>
	Most Recent Joe Steer Image:
	<br>
	<?php
		$takefrom_dir = "uploads/";
		$images = glob($takefrom_dir."*.jpg");
		if (sizeof($images) == 0){
		$images = glob($takefrom_dir."*png"); }
		$image = $images[0];
		echo '<img src="'.$image.'" width="400" height="600"/>';
		
		if (sizeof($images) > 1){
			array_shift($images);
		foreach($images as $image) {
			echo '<img src="'.$image.'" width="100" height="150"/>'; }
		}
	?>
</div>
</html>
<?php
	//log user data so i can block pk
	$log = array('time' => time(), 'ip' => $_SERVER['REMOTE_ADDR'], 'url' => $_SERVER['REQUEST_URI']);
	$openuserlog = fopen("userlog.txt", "r+");
	fwrite($openuserlog, $log);
	fclose($openuserlog);
?>
<html>
<div class="pkimg">
	<br>
	<h2>Illegal People:</h2>
	<img src="pk.JPG" width="120" height="100" />
</div> 
</html>
<div class="nonogram">
	<br>
	<a href="https://www.nonograms.org/nonograms2/i/7291">Monthly Nonogram:</a>
	<br>
	<img src="nonogram.JPG" width="600" height="600" href="www.nonograms.org/nonograms2/i/7291" /img>
</div>
