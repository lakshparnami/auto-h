<?php

$pin = urldecode($_POST['pin']);

$con = mysqli_connect("localhost","root","lucifer123");
$x = mysqli_select_db($con,"autoH");

if(!$con){
	die("Cannot setup connection: ". mysqli_connect_error());
}

$query = "delete from user where pin='$pin'";
$result = mysqli_query($con,$query);

if($result){
	$query = "delete from pref where pin='$pin'";
	$result = mysqli_query($con,$query);
	if($result){
		echo "User Successfully Deleted";
	}
}
else{
	echo "Problem in Deletion. Probably coder's fault..";
}


?>
