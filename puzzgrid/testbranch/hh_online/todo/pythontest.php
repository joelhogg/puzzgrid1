<html>
    <head>
        <meta charset="utf-8">
        <title>HH-OL</title>
    </head>
</html>

<?php
	$recv_val = $_POST['pythoninput'];
	echo "<center><h5>Query: " . "'" . $recv_val . "'" . "</h5></center>";
	echo "<br><br>";
	$result = shell_exec('py -3.6 wolframtest1.py' . " " . '"' . $recv_val . '"'); //maybe the extra thing here is the problem
	echo "<center><h3>" . $result . "</h3></center>";
?>