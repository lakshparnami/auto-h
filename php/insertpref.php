<?php

$pin = urldecode($_POST['pin']);
$l1 = urldecode($_POST['l1']);
$l2 = urldecode($_POST['l2']);
$l3 = urldecode($_POST['l3']);
$l4 = urldecode($_POST['l4']);
$f1 = urldecode($_POST['f1']);
$f2 = urldecode($_POST['f2']);
$voice = urldecode($_POST['voice']);

$con = mysqli_connect("localhost","root","lucifer123");
$x = mysqli_select_db($con,"autoH");

if(!$con){
	die("Cannot setup connection: ". mysqli_connect_error());
}

$query="insert into pref (pin,l1,l2,l3,l4,f1,f2,voiceservice) values('$pin','$l1','$l2','$l3','$l4','$f1','$f2','$voice')";
$result=mysqli_query($con,$query);

if($result){
		echo "Insertion successful";
}
else{
		echo "Problem";
}
?>
