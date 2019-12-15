<?php
  $nq = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $n = $nq[0];
  $q = $nq[1];

  # セグ木のノード数は「初めてn以上になる2のべき乗」*2-1
  # ノードをi, 木の最下部の列数をmとしたとき
  # i + m - 1が実際のノードということになる

  $m = 1;
  while($m < $n){
    $m *= 2;
  }
  $INF = pow(2, 31) - 1;
  $tree = array_fill(0, 2 * $m-1, $INF);

  function update($a, $b){
    global $tree, $n, $m;
    $a += $m - 1;
    $tree[$a] = $b;
    while($a > 0){
      $a = floor(($a - 1)/2);
      $tree[$a] = min($tree[2 * $a + 1], $tree[2 * $a + 2]);
    }
  }

  function find($a, $b, $l, $r, $k=0){
    global $tree, $n, $INF;
    if($r <= $a || $b <= $l){
      return $INF;
    }
    if($a<=$l && $r<=$b){
      return $tree[$k];
    }else{
      $lv = find($a, $b, $l, floor(($l + $r) / 2), 2 * $k + 1);
      $rv = find($a, $b, floor(($l + $r) / 2), $r, 2 * $k + 2);
      return min($lv, $rv);
    }
  }

  for($i=0; $i<$q; $i++){
    $query = array_map("intVal", explode(" ", trim(fgets(STDIN))));
    $x = $query[1];
    $y = $query[2];
    if($query[0] == 0){
      update($x, $y);
    }else{
      echo find($x, $y+1, 0, $m) . PHP_EOL;
      
    }
  }
?>