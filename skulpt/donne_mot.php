<?php

if ($_GET) {
    $dic = $_GET['dic'];
} else {
    $dic = "dico2";
}

$filename = "/var/www/skulpt/assets/".$dic.".txt";
$count = 0;

$lignes = file($filename);
$max = count($lignes);

$ligne = rand(0, $max);

if ( file_exists($filename) ) { 
    $fp = fopen($filename,"r");
    while(!feof($fp)) {
        $contenu = fgets($fp, 1024);
        if ($ligne == $count) {
             die(strtoupper($contenu));
        }
        $count++;

    }
    echo $count;
    fclose($fp);
}
?>