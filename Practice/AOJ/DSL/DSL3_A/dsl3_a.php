<?php
  $ns = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $n = $ns[0];
  $s = $ns[1];
  $arr = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $INF = pow(2, 31) - 1;
  $ans = $INF;

  $tmp = 0;
  $r = 0;
  for($l=0; $l<$n; $l++){
    while($r < $n && $tmp < $s){
      $tmp += $arr[$r];
      $r += 1;
    }
    if($tmp >= $s){
      $ans = min($ans, $r - $l);
    }
    if($r == $l){
      $r += 1;
    }else{
      $tmp -= $arr[$l];
    }
  }

  echo $ans != $INF ? $ans . PHP_EOL : 0 . PHP_EOL;
?>