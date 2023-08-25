<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <title>upload & send</title>
</head>
<body>
<form enctype="multipart/form-data" method="POST">
  <input type="file" name="img" accept="image/*"/>
  <input type="submit" value="upload"/>
</form>
<?php
$tmp_file = $_FILES['img']['tmp_name'];
if(move_uploaded_file($tmp_file,'./tmp.png')){
  echo "Uploaded completed.";
}
exec('bash send.sh',$return);
echo $return;
?>
</body>
</html>