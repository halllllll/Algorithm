<?php
  $n = intVal(trim(fgets(STDIN)));
  $arr = [];
  for($i=0; $i<$n; $i++){
    $input=explode(" ", trim(fgets(STDIN)));
    $arr[]= array("city"=>$input[0], "point"=>$input[1], "idx"=>$i+1);
  }
  array_multisort(array_column($arr, "city"), SORT_ASC, array_column($arr, "point"), SORT_DESC, $arr);
  foreach($arr as $a){
    echo $a["idx"] . PHP_EOL;
  }
?>