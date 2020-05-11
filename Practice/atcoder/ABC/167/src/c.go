package main

import "fmt"

var T [][]int
var C []int
var X, N int

func main() {
	var M int
	fmt.Scan(&N, &M, &X)
	T = make([][]int, N)
	C = make([]int, N)
	for i := 0; i < N; i++ {
		T[i] = make([]int, M)
		var V int
		fmt.Scan(&V)
		C[i] = V
		for j := 0; j < M; j++ {
			var V int
			fmt.Scan(&V)
			T[i][j] = V
		}
	}
	arr := make([]int, M)
	ans := rec(0, 0, arr)
	if ans == 10000000000000 {
		fmt.Println(-1)
	} else {
		fmt.Println(ans)
	}
}

func rec(i, cur int, arr []int) int {
	f := true
	for _, v := range arr {
		if v < X {
			f = false
		}
	}
	if f {
		return cur
	}
	if i == N {
		return 10000000000000
	}
	nex_arr := append([]int{}, arr...)
	for j, a := range T[i] {
		nex_arr[j] += a
	}
	nex_cur := cur + C[i]
	return min(rec(i+1, nex_cur, nex_arr), rec(i+1, cur, arr))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
