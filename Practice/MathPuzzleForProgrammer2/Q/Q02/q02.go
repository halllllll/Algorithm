package main

import (
	"fmt"
)

var start, goal, N uint

func main(){
	start, goal, N = 1, 17, 29
	cnt := 0
	// ビット演算
	// 1から17まで「取る」「取らない」の組み合わせの総数
	// (2~16までの15個の数列)
	cnt += 1<<(goal-start-1)
	// 29から17まで
	cnt += 1<<(N-goal)
	// 重複のぶん除外
	cnt--
	fmt.Println(cnt)
}