<?php
   $name = ["Sachin","Dhoni","Kohili","Sanju"];
	$size =sizeof($name);
   echo "<table border='1'>";
		echo "<tr>";
		echo	"<th>ID</th>";
		echo	"<th>name</th>";
		echo "</tr>";
	for($i = 0 ; $i<$size;$i++){
		echo"<tr>";
		echo"<td>$i</td>";
		echo"<td>$name[$i]</td>";
		echo"</tr>";
	}
?>