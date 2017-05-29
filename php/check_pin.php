<?php
	$pin = urldecode($_POST['pin']);


	$con = mysqli_connect("localhost","root","lucifer123");
	$x = mysqli_select_db($con,"autoH");

	if(!$con){
	
		die("Cannot setup connection: ". mysqli_connect_error());
	}


	$query = "select *` from user where pin='$pin'";
	$result = mysqli_query($con,$query);
	
	
	if(mysqli_num_rows($result)==1){
		echo "";
		$row = mysqli_fetch_assoc($result);
		if($row[admin]==1){
			echo "Logged in as Admin";
		}
		else{
			echo "Welcome bro".$row[name];
		}		
	}
	else
		echo "Porblem";

?>
