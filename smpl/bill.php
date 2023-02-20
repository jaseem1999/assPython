<html>
<head>
	<title>Elericity Bill</title>
</head>
<body>
	<form action="" method="POST">
		<lable>Enter the Unit</label>
		<input type="number" name="unit" placeholder="Enter the unit">
		<lable>Enter the Name</label>
		<input type="text" name="name" placeholder="Enter the Name">
		<lable>Enter the consumer no </label>
		<input type="number" name="no" placeholder="Enter the consumer no">
		<input type="submit" value="OK">
	</form>
<?php
	$conn = new mysqli("localhost","root","Love1999@MySQL","ebill");
	if($conn -> connect_error){
		echo "error ".connect_error;
	}
	if($_SERVER["REQUEST_METHOD"] == "POST"){
		$unit = $_POST["unit"];
		$name = $_POST["name"];
		$cono = $_POST["no"];
		if($unit < 100){
			$unitRs=4; 
			echo "<br><p span='price'>unit price :: ",4,"rs</p></br>";
			$rs1 = $unit * $unitRs;
			$gst = $rs1*2/100;
			$rs =$gst + $rs1;
			echo "<table border='2'>";
			echo "<tr><th>Name</th><th>Consumer No</th><th>Unit</th><th>Amount per Unit</th><th>Amount</th><th>GST</th><th>Total Amount</th></tr>";
			echo "<tr><td>$name</td><td>$cono</td><td>$unit</td><td>$unitRs</td><td>$rs1</td><td>$gst</td><td>$rs</td></tr>";
			$sql = "insert into bills(name,consumer_no,unit,amount_unit,amount,gst,tatal_amount)value('$name','$cono','$unit','$unitRs','$rs1','$gst','$rs');";
			if(mysqli_query($conn,$sql)){
				echo "Insertion successfully";
			}else{
				echo "Insertion failed";
			}
		}else{
			$unitRs=6; 
			echo "<br><p span='price'>unit price :: $unitRs rs</p></br>";
			$rs1 = $unit * $unitRs;
			$gst = $rs1*8/100;
			$rs =$gst + $rs1;
			echo "<table border='2'>";
			echo "<tr><th>Name</th><th>Consumer No</th><th>Unit</th><th>Amount per Unit</th><th>Amount</th><th>GST</th><th>Total Amount</th></tr>";
			echo "<tr><td>$name</td><td>$cono</td><td>$unit</td><td>$unitRs</td><td>$rs1</td><td>$gst</td><td>$rs</td></tr> ";
			echo "</table></br></br>";
			$sql = "insert into bills(name,consumer_no,unit,amount_unit,amount,gst,tatal_amount)value('$name','$cono','$unit','$unitRs','$rs1','$gst','$rs');";
			if(mysqli_query($conn,$sql)){
				echo "Insertion successfully";
			}else{
				echo "Insertion failed";
			}
		}
	}else{
	}
	$sql1 = "select * from bills";
	$result = $conn->query($sql1);
	if($result->num_rows > 0){
		echo "<table border='2'>";
		echo "<tr><th>Name</th><th>Consumer No</th><th>Unit</th><th>Amount per Unit</th><th>Amount</th><th>GST</th><th>Total Amount</th></tr>";
		while($rows = $result-> fetch_assoc()){
			echo "<tr>";
				echo "<td>".$rows['name']."</td>";
				echo "<td>".$rows['consumer_no']."</td>";
				echo "<td>".$rows['unit']."</td>";
				echo "<td>".$rows['amount_unit']."</td>";
				echo "<td>".$rows['amount']."</td>";
				echo "<td>".$rows['gst']."</td>";
				echo "<td>".$rows['tatal_amount']."</td>";
			echo "</tr>";
		}
		echo "</table></br></br>";
	}


?>
</body>
</html>