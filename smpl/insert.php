<html>
<head>
	<title>form </title>
</head>
<form action="" method="POST">
    <table>
        <tr>
            <td>Name</td>
            <td><input type="text" name="n"></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><input type="text" name="email"></td>
        </tr>
        <tr>
            <td>Password</td>
            <td><input type="password" name="password"></td>
        </tr>
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="submit"></td>
        </tr>
    </table>

</form>
<?php
// Database credentials
$host = "localhost";
$user = "root";
$pass = "Love1999@MySQL";
$db = "phpprogram";
// Connect to MySQL
$conn = new mysqli($host,$user,$pass,$db);
if($conn->connect_error){
	echo "connection failed".connct_error;
}else{
	if($_SERVER["REQUEST_METHOD"] == "POST"){
		$name =$_POST["n"];
		$email =$_POST["email"];
		$pass =$_POST["password"];
		$sql = "insert into registration(name,email,password)value('$name','$email','$pass')";
		if(mysqli_query($conn, $sql)){
			echo"<H1> Insertion Successfully</h1>";
		}else{
			echo"<H1> Insertion Failed</h1>";
		}
	}
}

?>