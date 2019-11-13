<?php
  // 雰囲気的に最小公倍数をアレすればいけそう 雰囲気的に
  // せっかく取得したxを配列にぶちこんで（インデックスとか無視して）ソートするところがミソ
  
  $nx = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $n = $nx[0];
  $x = $nx[1];
  $arr = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $arr[] = $x;
  sort($arr);

  $dif = [];
  for($i=0; $i<$n; $i++){
    $dif[] = $arr[$i+1] - $arr[$i];
  }
  
  function gcd($x, $y){
    if($x > $y) return gcd($y, $x);
    if($x == 0) return $y;
    $tmp = $y % $x;
    $y = $x;
    $x = $tmp;
    return gcd($x, $y);
  }

  function lcm($x, $y){
    return intVal(($x * $y) / gcd($x, $y));
  }

  $gcdn = $dif[0];
  for($i=1; $i<$n; $i++){
    $gcdn = gcd($gcdn, $dif[$i]);
  }

  echo $gcdn . PHP_EOL;
?>