<?php
	$pin = urldecode($_POST['pin']);


	$con = mysqli_connect("localhost","root","lucifer123");
	$x = mysqli_select_db($con,"autoH");

	if(!$con){
	
		die("Cannot setup connection: ". mysqli_connect_error());
	}


	$query = "select pin, name from user where pin='$pin'";
	$result = mysqli_query($con,$query);
	
	
	if(mysqli_num_rows($result)==1){
		echo "Pin is correct";		
	}
	else
		echo "Porblem";

?>
