<?php
  // 差が1以内のみ可能。
  // 差が0のときは oxoxoxとxoxoxo, 1のときはoxoxoのみ
  $nm = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $n = $nm[0];
  $m = $nm[1];
  $inf = pow(10, 9) + 7;
  if(abs($n - $m)>1){
    echo 0 . PHP_EOL;
  }elseif($n == $m){
    $x = 1;
    for($i=1; $i<=$n; $i++){
      $x = ($x * $i)%$inf;
    }
    echo (($x*$x)%$inf*2)%$inf . PHP_EOL;
  }else{
    $x = 1;
    $y = 1;
    for($i=1; $i<=max($n, $m); $i++){
      $x = ($x * $i)%$inf;
    }
    for($i=1; $i<=min($n, $m); $i++){
      $y = ($y * $i)%$inf;
    }
    echo ($x*$y)%$inf . PHP_EOL;
  }
?>