<?php
$dir = '/opt/sharkshadows/img/samples/shark';
$files = glob("$dir/*.{jpg,png,gif,JPG,JPEG}", GLOB_BRACE);
foreach($files as $file) {
  inspect($file);
}

function inspect($filename){
  $dims = getimagesize($filename);
  echo "$filename\t1\t0 0 {$dims[0]} {$dims[1]}\n";
}
?>
