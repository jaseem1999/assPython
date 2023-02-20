<h1 style="text-align:center;">Employees salary details</h1>
<form style="text-align: -webkit-center;"  action = "" method="POST">
	<table>
		<tr>
			<td><label>Name</label></td>
			<td><input type="text" name="name"></td>
		</tr>
		<tr>
			<td><label>Basic Salary</label></td>
			<td><input type="number" name="salary"></td>
		</tr>
		<tr>
			<td><label>Bond</label></td>
			<td><input type="number" name="bond"></td>
		</tr>
		<tr>
			<td colspan='2'><input style="text-align: -webkit-center;"  type="submit" value="Submit"></td>
		</tr>
	</table>
</form>

<?php
	$conn = new mysqli("localhost","root","Love1999@MySQL","ebill");
	if($conn -> connect_error){
		echo "Connection error".connect_error;
	}
	if($_SERVER["REQUEST_METHOD"]=="POST"){
		$name = $_POST["name"];
		$bs = $_POST["salary"];
		$b = $_POST["bond"];
		$ts = $bs + $b;
		$tsy = $ts*12;
		$tax = 0;
		$salary = 0;	
		if($tsy>500000){
			$c=$tsy-500000;
			$tax = $c * 30/100;
			$salary = $tsy - $tax;
		}
		echo "<h2 style='text-align:center;'>Employees salary details ".$name."</h2>";
		echo "<table border='2' style='margin: auto;'";
		echo "<tr>";
			echo "<th>Name</th><th>Salary</th><th>Others</th><th>Salary(month)</th><th>Salary(year)</th><th>Tax</th><th>Net Salary</th>";
		echo "</tr>";
		echo "<tr>";
			echo "<th>$name</th><th>$bs</th><th>$b</th><th>$ts</th><th>$tsy</th><th>$tax</th><th>$salary</th>";
		echo "</tr>";
		echo "</table>";
		$sql = "insert into salary(name,salary,others,salary_month,salary_year,tax,net_salary)value('$name','$bs','$b','$ts','$tsy','$tax','$salary');";
		if(mysqli_query($conn,$sql)){
			echo "insertion successfully";
		}else{
			echo "insertion failed";
		}
	}
	echo"<h2 style='text-align:center;'>Employees salary details</h2>";
	$sql1="select * from salary;";
	$result = $conn->query($sql1);
	if($result->num_rows > 0){
		echo "<table border='2' style='margin: auto;'";
		echo "<tr>";
			echo "<th>Name</th><th>Salary</th><th>Others</th><th>Salary(month)</th><th>Salary(year)</th><th>Tax</th><th>Net Salary</th>";
		echo "</tr>";
		while($row = $result -> fetch_assoc()){
			echo "<tr>";
			echo "<td>".$row['name']."</td>";
			echo "<td>".$row['salary']."</td>";
			echo "<td>".$row['others']."</td>";
			echo "<td>".$row['salary_month']."</td>";
			echo "<td>".$row['salary_year']."</td>";
			echo "<td>".$row['tax']."</td>";
			echo "<td>".$row['net_salary']."</td>";
			echo "</tr>";
		}
	}
?>