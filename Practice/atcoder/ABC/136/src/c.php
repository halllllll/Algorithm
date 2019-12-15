<?php
  // 逆からみて単調非増加
  
  $n = intVal(trim(fgets(STDIN)));
  $arr = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  for($i=$n-2; $i>=0; $i--){
    if($arr[$i]-$arr[$i+1] > 1){
      echo "No" . PHP_EOL;
      exit();
    }elseif($arr[$i] - $arr[$i+1] == 1){
      $arr[$i] -= 1;
    }
  }
  echo "Yes" . PHP_EOL;
?>