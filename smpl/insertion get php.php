<form action="" method="POST">
    <label for="">Name</label>
    <input type="text" name="name">
    <input type="submit" value="Submit">
</form>
<?php
$conn = new mysqli("localhost", "root", "Love1999@MySQL", "cricket");
if($conn->connect_error){
    die("Connection failed: " . $conn->connect_error);
}
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $name = $_POST["name"];
    $sql = "insert into players(name) value('$name');";
    if(mysqli_query($conn, $sql)){
        echo "Insertion successfully";
    }else{
        echo "Insertion failed";
    }
}
$sql1 = "select * from players";
$result = $conn->query($sql1);
if($result->num_rows > 0){
    echo "<table border='2'>";
    echo "<tr><th>Name</th></tr>";
    while($rows = $result-> fetch_assoc()){
        echo "<tr>";
            echo "<td>".$rows['name']."</td>";
        echo "</tr>";
    }
    echo "</table>";
}