<?php
	$email = urldecode($_POST['email']);
	$name = urldecode($_POST['name']);
	$phone = urldecode($_POST['phno']);
	$auth = urldecode($_POST['auth']);
	$pin = urldecode($_POST['pin']);


	$con = mysqli_connect("localhost","root","lucifer123");
	$x = mysqli_select_db($con,"autoH");

	if(!$con){
	
		die("Cannot setup connection: ". mysqli_connect_error());
	}


	$query = "insert into user(email,name,phone,pin) values('$email','$name','$phone','$pin')";
	$result = mysqli_query($con,$query);

	if($result){
		echo "Insertion successful";
	}

	else{
		echo "Problem aa gayi lodu";
		echo $phone;
	}
	

?>