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
	
	$q1 = "select * from user where pin='$pin'";
	$res = mysqli_query($con,$q1);
	$q2 = "select * from user where email='$email'";
	$res2 = mysqli_query($con,$q2);
	
	if(mysqli_num_rows($res)>0){
		echo "Choose a unique pin.";
	}
	elseif(mysqli_num_rows($res2)>0){
			echo "Email Exists";
	}
	else{
		$query = "insert into user(email,name,phone,pin,admin) values('$email','$name','$phone','$pin','$auth')";
		$result = mysqli_query($con,$query);

		if($result){
			echo "Insertion successful";
		}

		else{
			echo "Problem";
		}
	}
	
	

?>
