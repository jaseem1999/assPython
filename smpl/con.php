<?php
	$host = "localhost";
	$user = "root";
	$pass = "Love1999@MySQL";
	$db = "emp_crud";
	$conn = new mysqli($host,$user,$pass,$db);
	if($conn ->connect_error){
		die("Connection failed ".$conn->connect_error);
	}
	$sql = "select * from user_table";
	$rs = $conn->query($sql);
	if ($rs->num_rows > 0){
	echo"<table border='1'>";
		while ($row = $rs->fetch_assoc()){
				echo "<tr>";
 					echo "<td>" . $row["id"] . "</td>";
 					echo "<td>" . $row["name"] . "</td>";
 					echo "<td>" . $row["email"] . "</td>";
				 echo "</tr>";
		}
	echo"</table>";	
	}
?>