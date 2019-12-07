<?php
  # pythonで解けない時はphpでやるわ
  # TLEなる.... python以下ですか
  $N = intVal(fgets(STDIN));
  $graph = array_fill(0, $N-1, array());
  for($i=0; $i<$N-1; $i++){
    $abc = array_map("intVal", explode(" ", fgets(STDIN)));
    $a = $abc[0]-1;
    $b = $abc[1]-1;
    $c = $abc[2];
    $graph[$a][] = ["node"=>$b, "weight"=>$c];
    $graph[$b][] = ["node"=>$a, "weight"=>$c];
  }
  # print_r($graph);
  $qk = array_map("intVal", explode(" ", fgets(STDIN)));
  $q = $qk[0];
  $k = $qk[1] - 1;
  $ans_list = array_fill(0, $N-1, 0);


  function dfs($node, $used, $weight){
    global $graph, $N, $ans_list;
    foreach($graph[$node] as $data){
      if(!in_array($data["node"], $used, true)){
        $next_used = $used;
        $next_used[]= $data["node"];
        $i+=1;
        dfs($data["node"], $next_used, $weight + $data["weight"]);
      }
    }
    $ans_list[$node] = $weight;
  }

  $arr = [$k];
  dfs($k, $arr, 0);
  for($i=0; $i<$q; $i++){
    $ab = array_map("intVal", explode(" ", fgets(STDIN)));
    $a = $ab[0] - 1;
    $b = $ab[1] - 1;
    echo $ans_list[$a] + $ans_list[$b] . PHP_EOL;
  }
?>