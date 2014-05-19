<?php
if ($_GET) {
  extract($_GET);
  if ($sender) {
     if ($sender == 'codeskulptor-MrT') {
          //todo lires les fichiers pythons
    
    $path = "/var/www/skulpt/python/";

    $filename = $path."".$id.".py";
    echo "#".$id."\n";
    $text = "Author: M. TACK Sébastien, prof. certifie de TECHNOLOGIE";
    echo "#".$text."\n";
    $text = "mailTo: sebastien.tack@ac-caen.fr";
    echo "#".$text."\n";
    echo "#\n";

    if ( file_exists($filename) ) { 
         $fp = fopen($filename,"r");
         while(!feof($fp)) {
         $contenu = fgets($fp, 1024);
         echo $contenu;
         //$infos=explode('\n', $contenu);
         //print_r($infos);
         
	 }
         fclose($fp);
        } 
    } else {
          
          exit();
}
  }
}
?>
