<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <title>upload & compile & send</title>
</head>
<body>

<form enctype="multipart/form-data" method="POST" action="">
  <input type="file" name="img" accept="image/*"/>
  <input type="submit" value="upload"/>
</form>

<?php
switch($_FILES['img']['error']){
  case UPLOAD_ERR_OK:
    break;
  case UPLOAD_ERR_NO_FILE:
    echo 'no file';
    break;
  default:
    echo 'File upload error:'.$_FILES['img']['error'];
}
$tmp_file = $_FILES['img']['tmp_name'];
if(move_uploaded_file($tmp_file,'./tmp.png')){
  echo "Uploaded.";
  echo '<img src="tmp.png">';
  exec('bash ./send.sh',$return);
}else{
  echo "file preparation error.";
}
?>

</body>
</html>