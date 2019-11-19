<?php
  $n = intval(trim(fgets(STDIN)));

  function luca($n){
    $a = 2;
    $b = 1;
    $i = 1;
    while($i < $n){
      $tmp = $a;
      $a = $b;
      $b = $tmp + $b;
      $i += 1;
    }
    return $b;
  }

  echo luca($n) . PHP_EOL;
?>