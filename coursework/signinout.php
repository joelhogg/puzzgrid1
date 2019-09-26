<?php
if (isset($_POST['signin_button'])) {
	$inout = "in";
}
elseif (isset($_POST['signout_button'])) {
	$inout = "out";
}
$username = 0;
$password = 0;

$check = $_COOKIE["check"];
if ($check == "True") {
	$username = $_COOKIE["username"];
	$password = $_COOKIE["password"];
	$result = shell_exec("py -3.7 python_recv.py " .$username ." " .$password ." " .$inout);
	if ($result == 1) {
		$sucsess_check = 1;
		//echo "Signed " .$inout ." sucsessfully!";
	}
	else {
		echo $result;
	}
}
?>
<script>
	function setCookie(name,value){
		document.cookie=(name+"="+escape(value));
	}
	
	var suc_check = `<?php echo $sucsess_check; ?>`;
	var in_out = `<?php echo $inout; ?>`;
	
	if (suc_check == 1) {
		setCookie("inout_status",in_out);
		history.go(-1);
	}
</script>

