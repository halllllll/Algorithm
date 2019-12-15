<?php
  $n = intval(trim(fgets(STDIN)));
  $arr = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $arr = array_reverse($arr);
  $ans = array_fill(0, $n, 0);
  for($i=1; $i<$n; $i++){
    if($arr[$i] >= $arr[$i-1]){
      $ans[$i] = $ans[$i-1] + 1;
    }
  }
  echo max($ans) . PHP_EOL;
?>