<?php
  # めんどくせぇしどうせPHPなので果敢にevalを使う（evil <- PHPのevalが意味不明な挙動しやがるので諦めて愚直にやる
  $number = array_map("intVal", str_split(trim(fgets(STDIN))));
  $op = ["+", "-"];
  foreach($op as $x){
    foreach($op as $y){
      foreach($op as $z){
        // PHPのevalがなんか意味不明な挙動をしやがる
        // # $ans = "$number[0] $x $number[1] $y $number[2] $z $number[3]";
        // # echo "ans = $ans, sum = " . eval($ans) . PHP_EOL;
        // echo eval("return " . $ans . ";") . PHP_EOL;
        // ので諦める
        $ans = 0;
        if($x=="+"){
          $ans += ($number[0]) + ($number[1]);
        }else{
          $ans += ($number[0]) - ($number[1]);
        }
        if($y=="+"){
          $ans += ($number[2]);
        }else{
          $ans -= ($number[2]);
        }
        if($z=="+"){
          $ans += ($number[3]);
        }else{
          $ans -= ($number[3]);
        }
        if($ans == 7){
          echo "${number[0]}${x}${number[1]}${y}${number[2]}${z}${number[3]}" . "=7" . PHP_EOL;
          exit();
        }
      }
    }
  }
?>