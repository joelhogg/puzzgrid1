<?php
	$username = $_POST["username"];
	$password = $_POST["password"];
	
	$username = strtolower($username);
	
	$result = shell_exec("py -3.7 python_recv.py " .$username ." " .$password ." none");
	if ($result == 1) {
		//setcookie("username,".$username."/password=".$password);
		//function setCookie(name,value){document.cookie=name+"="+escape(value)+"; path=/; expires="+expiry.toGMTString();}
	}
	else {
		//document.cookie = ("null");
	}
?>
<script>
	function setCookie(name,value){
		document.cookie=(name+"="+escape(value));
	}
	var vResult = `<?php echo $result ?>`;
	if (vResult == 1) {
		var vUsername = `<?php echo $username ?>`;
		var vPassword = `<?php echo $password ?>`;
		
		setCookie("check","True");
		setCookie("username",vUsername);
		setCookie("password",vPassword);
		
		history.go(-2);
	}
	
	else {
		setCookie("check", "False");
	}
</script>