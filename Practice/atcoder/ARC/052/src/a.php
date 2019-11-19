<?php
  function f($x){
    return is_numeric($x) ? true : false;
  }
  echo implode(array_filter(str_split(trim(fgets(STDIN))), "f")) . PHP_EOL;
?>