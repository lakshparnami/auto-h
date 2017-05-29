<?php

$pin = urldecode($_POST['pin']);
$l1 = urldecode($_POST['l1']);
$l2 = urldecode($_POST['l2']);
$l3 = urldecode($_POST['l3']);
$l4 = urldecode($_POST['l4']);
$f1 = urldecode($_POST['f1']);
$f2 = urldecode($_POST['f2']);

$con = mysqli_connect("localhost","root","lucifer123");
$x = mysqli_select_db($con,"autoH");

if(!$con){
	die("Cannot setup connection: ". mysqli_connect_error());
}

$query="update pref set l1='$l1', l2='$l2', l3='$l3', l4='$l4', f1='$f1', f2='$f2' where pin='$pin'";
$result=mysqli_query($con,$query);

if($result){
	echo "Updation successful";
}
else{
	echo "Problem";
}
?>

