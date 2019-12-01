<?php
  $n = intVal(trim(fgets(STDIN)));
  $s = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $color = 0;
  $ans = 1;
  $MOD = 1000000007;
  $cur = [-1, -1, -1];

  if($s[0] != 0){
    echo 0 . PHP_EOL;
    exit();
  }
  foreach($s as $c){
    if($c == 0){
      if($color >= 3){
        echo 0 . PHP_EOL;
        exit;
      }
      $cur[$color] = 0;
      $color += 1;
      $ans %= $MOD;
    }else{
      $x = 0;
      foreach($cur as $curn){
        if($curn == $c-1){
          $x += 1;
        }
      }
      if($x == 0){
        echo 0 . PHP_EOL;
        exit();
      }
      $ans *= $x;
      $ans %= $MOD;
      $idx = array_search($c-1, $cur);
      $cur[$idx] += 1;
    }
  }

  if($color == 0){
    $ans *= 1;
  }elseif($color == 1){
    $ans *= 3;
  }else{
    $ans *= 6;
  }
  $ans %= $MOD;
  echo $ans . PHP_EOL;
?>