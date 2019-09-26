<?php
$targetdir = "uploads/";
$goodupload = 1;
$postedfile = $targetdir . basename($_FILES["filetoupload"]["name"]);
$filetype = strtolower(pathinfo($postedfile,PATHINFO_EXTENSION));

if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["filetoupload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $goodupload = 1;
    } else {
        echo "File is not an image.";
        $goodupload = 0;
    }
}
if($filetype!= "jpg" && $filetype != "png" && $filetype != "jpeg"
&& $filetype != "ico" ) {
    echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
    $uploadOk = 0;
}

if ($goodupload == 1){
	if (move_uploaded_file($_FILES["filetoupload"]["tmp_name"], $postedfile)) {
        echo "The file ". basename( $_FILES["filetoupload"]["name"]). " has been uploaded.";
    }
	else { echo "Sorry, there was an error uploading your file."; }
	echo "file has been uploaded!";
}


?>
