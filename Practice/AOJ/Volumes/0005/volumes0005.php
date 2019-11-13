<?php
    # 完全にシステムのバグだと思うんだけどなんかしらんけど
    # これだと意味不明な Presentation Error とかいうバグが出る

    function gcd($x, $y){
        if($x > $y){
            return gcd($y, $x);
        }
        if($x == 0){
            return $y;
        }
        $tmp = $y % $x;
        $y = $x;
        $x = $tmp;
        return gcd($x, $y);
    }
    
    function lcm($x, $y){
        return ($x * $y) / gcd($x, $y);
    }
    
    
    while($ab = (fgets(STDIN))){
        // PHP stdin is so fuck
        if(!$ab)break;
        $ab = array_map("intVal", explode(" ", trim($ab)));
        $a = $ab[0];
        $b = $ab[1];
            
        echo gcd($a, $b) . " " . lcm($a, $b) . PHP_EOL;
    }
?>
