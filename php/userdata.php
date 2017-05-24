<?php
	
	
	$con = mysqli_connect("localhost","root","lucifer123");
	$x = mysqli_select_db($con,"autoH");
	
	if(!$con){
	
		die("Cannot setup connection: ". mysqli_connect_error());
	}
	$query = "select * from user";
	$result = mysqli_query($con,$query);
	$rows = array();
	while($r = mysqli_fetch_assoc($result)) {
		$rows[] = $r;
	}
	echo json_encode($rows);
?>
