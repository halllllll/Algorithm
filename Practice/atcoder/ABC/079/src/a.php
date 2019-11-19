<?php
  # 前もしくは後ろ3つを確認
  $s = str_split(trim(fgets(STDIN)));
  $pro1 = array_slice($s, 0, 3);
  $pro2 = array_slice($s, 1, 3);
  $pro1 = array_unique($pro1);
  $pro2 = array_unique($pro2);
  
  if(count($pro1) == 1 || count($pro2) == 1){
    echo "Yes" .  PHP_EOL;
  }else{
    echo "No" . PHP_EOL;
  }
?>