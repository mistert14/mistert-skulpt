<?php
error_reporting(E_ALL);

if ($_POST) {
    echo "Updating ...";
  
	$test = exec("/var/www/skulpt/update.sh" ,$output,$return_var );
    //print_r($output);
    print_r($return_var);
    //print_r($test);

}
?>
<html>
<head></head>
<body>
<form name="form1" method="post" action="update.php">
<input type="hidden" name="nom"></input>
<input type="submit" value="Update Skulpt"></input>
</form>
</body>
</html>
