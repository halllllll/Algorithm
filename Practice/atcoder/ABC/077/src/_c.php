<?php
  # にぶたんのいい問題らしいぞ もう以前どうやって解いたかとか忘れたけど
  $n = intVal(trim(fgets(STDIN)));
  $as = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $bs = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  $cs = array_map("intVal", explode(" ", trim(fgets(STDIN))));
  sort($as);
  sort($bs);
  sort($cs);

  function lower_bound($t, $arr){
    $l = 0; 
    $r = count($arr);
    while($l < $r){
      $mid = floor(($l + $r) / 2);
      if($arr[$mid] > $t){
        $r = $mid;
      }else{
        $l = $mid + 1;
      }
    }
    return $r;
  }

  $ans = 0;
  foreach($as as $a){
    $b = lower_bound($a, $bs);
    $c = lower_bound($b, $cs);
    $ans += $b*$c;
  }
  echo $ans . PHP_EOL;
?>