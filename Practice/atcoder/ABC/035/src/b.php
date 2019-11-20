<?php
  // ?はいつ動いてもいいので最後に動かす
  // というか動かす必要すらない
  // 最小値の取扱いに注意 2重に罠があった

  $s = str_split(trim(fgets(STDIN)));
  $t = trim(fgets(STDIN));
  $drone_pos = ["x" => 0, "y" => 0];
  $free_count = 0;

  foreach($s as $c){
    switch($c){
      case "U":
        $drone_pos["y"]+=1;
        break;
      case "D":
        $drone_pos["y"]-=1;
        break;
      case "R":
        $drone_pos["x"]+=1;
        break;
      case "L":
        $drone_pos["x"]-=1;
        break;
      case "?":
        $free_count += 1;
        break;
    }
  }

  $dist = abs($drone_pos["x"]) + abs($drone_pos["y"]);
  if($t == "1"){
    echo $dist + $free_count . PHP_EOL;
  }else{
    if($dist < $free_count){
      if(($free_count - $dist) % 2 == 0){
        echo 0 . PHP_EOL;
      }else{
        echo 1 . PHP_EOL;
      }
    }else{
    echo $dist - $free_count . PHP_EOL;
    }
  }
?>