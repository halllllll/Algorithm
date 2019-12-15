完全に意味不明なんだけどなぜかWAなる
<?php
  // 尺取典型
  $nk = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $n = $nk[0];
  $k = $nk[1];
  $arr = [];
  for($i=0; $i<$n; $i++){
    $t = intVal(trim(fgets(STDIN)));
    if($t == 0){
      echo $n . PHP_EOL;
      exit();
    }
    $arr[] = $t;
  }
  $l = 0;
  $r = 0;
  $ans = 0;
  $tmp = 1;
  while($r < $n-1){
    if($tmp * $arr[$r+1] <= $k){
      $tmp *= $arr[$r+1];
      $r += 1;
      // ansは長さなので
      $ans = max($ans, $r - $l);
    }elseif($r == $l){
      $r += 1;
      $l += 1;
    }else{
      $tmp /= $arr[$l];
      $l += 1;
    }
  }
  echo $ans . PHP_EOL;
?>