<?php
  // 手元で試したら abs(a*b-(a*2 + b*2) + 4)が浮かんだ
  // ちゃんと計算すると、偶数回訪れるマスは表、奇数回なら裏になる
  // 一番外周は偶数回になる（4隅は4回、辺は6回、それ以外の内側は9回）
  // なのでそれを引く
  $ab = array_map("intVal", explode(" ", fgets(STDIN)));
  $a = $ab[0];
  $b = $ab[1];
  echo abs($a * $b - ($a*2+$b*2) + 4) . PHP_EOL;
?>