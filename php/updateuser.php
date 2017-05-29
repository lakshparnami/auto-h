<?php

$email = urldecode($_POST['email']);
$name = urldecode($_POST['name']);
$phone = urldecode($_POST['phno']);
$auth = urldecode($_POST['auth']);
$newpin = urldecode($_POST['newpin']);
$oldpin = urldecode($_POST['oldpin']);

$con = mysqli_connect("localhost","root","lucifer123");
$x = mysqli_select_db($con,"autoH");

if(!$con){
	die("Cannot setup connection: ". mysqli_connect_error());
}

$query = "update user set email='$email' , name='$name' , phone='$phone' , admin='$auth' , pin='$newpin' where pin='$oldpin'";
$result = mysqli_query($con,$query);

if($result){
	echo "Successfully updated";
}
else{
	echo "$query";
}


?>
