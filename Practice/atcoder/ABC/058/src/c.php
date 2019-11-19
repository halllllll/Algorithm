<?php
  # 最初のに合わせて最小値を更新していく方針
  $n = intVal(trim(fgets(STDIN)));
  $first = str_split(trim(fgets(STDIN)));
  $fix = [];
  foreach($first as $k=>$v){
    if(array_key_exists($v, $fix)){
      $fix[$v] += 1;
    }else{
      $fix[$v] = 1;
    }
  }
  for($i = 1; $i < $n; $i++){
     $next = str_split(trim(fgets(STDIN)));
     $next_count_values = array_count_values($next);
     foreach($fix as $k=>$v){
       if(array_key_exists($k, $next_count_values)){
         $fix[$k] = min($fix[$k], $next_count_values[$k]);
       }else{
         unset($fix[$k]);
       }
     }
  }
  ksort($fix);
  $ans = "";
  foreach($fix as $k=>$v){
    for($i=0; $i<$v; $i++){
      $ans .= $k;
    }
  }
  echo $ans . PHP_EOL;
?>