<?php
	$a = 10;
	$b = 20;
	echo "before swapping a is $a and b is $b <br>";
	$a = $a + $b;
	$b = $a - $b;
	$a = $a - $b;
	echo "after swapping a is $a and b is $b";
?>