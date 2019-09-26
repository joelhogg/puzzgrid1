<?php
	$adminpassword = $_POST["adminpassword"];
	$sleepstatuschoice = $_POST["sleepstatuschoice"];
	
	$storedpassword = file("password.txt");
	$storedpassword = $storedpassword[0];
	
	if ($adminpassword == $storedpassword){
		if ($sleepstatuschoice == "awake"){
			$writenewstatus = fopen("sleepstatusfile.txt", "r+");
			fwrite($writenewstatus, "awake ");
			fclose($writenewstatus);
		}
		else if ($sleepstatuschoice == "asleep"){
			$writenewstatus = fopen("sleepstatusfile.txt", "r+");
			fwrite($writenewstatus, "asleep");
			fclose($writenewstatus);
		}
		echo "Status sucsessfully updated! \n joe is now:" . $sleepstatuschoice;
	}
?>
<script>
	makealertjs = '<?php echo $makealert; ?>'
	alert(makealertjs)
</script>

<form action="index.php">
	Go back to the Home Page: <input type="submit" value="Back">
</form>