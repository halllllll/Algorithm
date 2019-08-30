package main

import (
	"fmt"
)

func sum(a []int) (ret int) {
	for _, v := range a {
		ret += v
	}
	return
}

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		var x int
		fmt.Scan(&x)
		arr[i] = x
	}
	// なんとなくiまでとi-1までの和が1と-1が交互になるようにしてnが奇数だったら最初の数値には手を付けないみたいな感じ
	// i項までの和が0になったらいまみてる数値の符号だけインクリメントかデクリメントする
	res := append([]int{}, arr...)
	first := arr[0]
	ans := 0
	var minus bool
	if first < 0 {
		minus = true
	} else {
		minus = false
	}
	for i, v := range arr[1:] {
		/*
			i=1 -1
			i=2	-1+4=3
			i=3 3+3(-7)=-1 7回インクリメント
			i=4 -1+2 = 1
			i=5 1-5 = -4
			i=6 -4+4(+1) = 1 1回インクリメント
			結果
			-1 4 -7 1 -5 1
		*/
		var sum int
		if minus{
			if 0<sum(arr[:i+1]){
				minus != minus
				continue
			}else{
				
			}
		}
	}

}
