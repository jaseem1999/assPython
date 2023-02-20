<form action="" method="POST">
  <table>
    <tr><td><label for="name">ADS</label></td><td><input type="number" name="ads"></td></tr>
    <tr><td><label for="name">ASE</label></td><td><input type="number" name="ase"></td></tr>
    <tr><td><label for="name">MFC</label></td><td><input type="number" name="mfc"></td></tr>
    <tr><td><label for="name">DFCA</label></td><td><input type="number" name="dfc"></td></tr>
    <tr><td><input type="submit" value="Submit"></td></tr>
</form>
<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $ads = $_POST['ads'];
    $ase = $_POST['ase'];
    $mfc = $_POST['mfc'];
    $dfc = $_POST['dfc'];
    $total = $ads + $ase + $mfc + $dfc;
    $percentage = ($total/400)*100;
   echo "<table border='2'>";
    echo "<tr><td>ADS</td><td>$ads</td></tr>";
    echo "<tr><td>ASE</td><td>$ase</td></tr>";
    echo "<tr><td>MFC</td><td>$mfc</td></tr>";
    echo "<tr><td>DFCA</td><td>$dfc</td></tr>";
    echo "<tr><td>Total</td><td>$total</td></tr>";
    echo "<tr><td>Percentage</td><td>$percentage</td></tr>";
    echo "</table>";
}
?>