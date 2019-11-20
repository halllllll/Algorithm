<?php
  // 愚直に保存して数える
  $nk = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $n = $nk[0];
  $k = $nk[1];
  $table = [];
  for($i=0; $i<$n; $i++){
    $ab = array_map("intVal", explode(" ", trim(fgets(STDIN))));
    $a = $ab[0];
    $b = $ab[1];
    if(array_key_exists($a, $table)){
      $table[$a] += $b;
    }else{
      $table[$a] = $b; 
    }
  }
  ksort($table);
  $cur = 0;
  foreach($table as $tk=>$tv){
    if($k<=$cur+$tv){
      echo $tk . PHP_EOL;
      exit();
    }else{
      $cur += $tv;
    }
  }
?>