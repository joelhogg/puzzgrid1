<?php
   if(isset($_FILES['audiofile'])){
      $errors= array();
      $file_name = $_FILES['audiofile']['name'];
      $file_size = $_FILES['audiofile']['size'];
      $file_tmp = $_FILES['audiofile']['tmp_name'];
      $file_type = $_FILES['audiofile']['type'];
      $file_ext=strtolower(end(explode('.',$_FILES['audiofile']['name'])));
      
      $extensions= array("ogg","mp3","wav");
      
      if(in_array($file_ext,$extensions)=== false){
         $errors[]="extension not allowed, please choose a JPEG or PNG file.";
      }
      
      if($file_size > 2000000) {
         $errors[]='File size must be excately 2 MB';
      }
      
      if(empty($errors)==true) {
         move_uploaded_file($file_tmp,"audio_catcher/".$file_name);
         echo "Success";
      }else{
         print_r($errors);
      }
   }
   else {
	   echo "error, file is null";
   }
?>