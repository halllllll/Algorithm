// JOI 2011 qual4
// 左から攻めていく DP[i][j] := i-1番目までの計算結果がjになるような個数？
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	DP := make([][]int, N+10)
	for i := 0; i < len(DP); i++ {
		DP[i] = make([]int, 30)
	}
	// DP[0][A[0]] = 1 これがおかしかった....（なんで？
	DP[1][A[0]] = 1
	for i := 1; i <= N; /* 配るDPの場合 N-1*/ i++ {
		for j := 0; j < 30; j++ {
			// 貰うDP
			if j-A[i-1] >= 0 {
				DP[i][j] += DP[i-1][j-A[i-1]]
			}
			if j+A[i-1] <= 20 {
				DP[i][j] += DP[i-1][j+A[i-1]]
			}
			// ------配るDPでやってみる...（* iの上限はN-1にする）-------
			// if j-A[i] >= 0 {
			// 	DP[i+1][j] += DP[i][j-A[i]]
			// }
			// if j+A[i] <= 20 {
			// 	DP[i+1][j] += DP[i][j+A[i]]
			// }
		}
	}
	fmt.Println(DP[N-1][A[N-1]])

	// 以下はメモ化再帰
	memo := make(map[[2]int]int)
	var rec func(i, j int) int
	rec = func(i, j int) int {
		if _, ok := memo[[2]int{i, j}]; ok {
			return memo[[2]int{i, j}]
		}
		if i == N-1 {
			if j == A[N-1] {
				return 1
			}
			return 0
		}
		ret := 0
		if 0 <= j-A[i] {
			ret += rec(i+1, j-A[i])
		}
		if j+A[i] <= 20 {
			ret += rec(i+1, j+A[i])
		}
		memo[[2]int{i, j}] = ret
		return ret
	}
	// fmt.Println(rec(0, 0))
}
