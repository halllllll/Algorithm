<?php
  $arr = array_map(intval, explode(" ", trim(fgets(STDIN))));
  $n = $arr[0];
  $q = $arr[1];
  $parents = range(0, $n-1);

  function root($x){
    global $parents;
    if($x === $parents[$x]){
      return $x;
    }else{
      return $parents[$x] = root($parents[$x]);
    }
  }

  function same($x, $y){
    return root($x) == root($y);
  }

  function union($x, $y){
    global $parents;
    if(!same($x, $y)){
      $parents[root($x)] = $y;
    }
  }

  for($i=0; $i<$q; $i++){
    $query = array_map(intVal, explode(" ", trim(fgets(STDIN))));
    if($query[0] === 0){
      // unite
      union($query[1], $query[2]);
    }else{
      // is same
      echo same($query[1], $query[2]) ? 1 . PHP_EOL : 0 . PHP_EOL;
    }
  }
?>