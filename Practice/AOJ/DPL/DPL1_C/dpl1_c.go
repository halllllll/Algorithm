package main

import "fmt"

func main() {
	var N, W int
	fmt.Scan(&N, &W)
	DP := make([][]int, N+10)
	for i := 0; i < len(DP); i++ {
		DP[i] = make([]int, W+10)
	}
	Vs, Ws := make([]int, N), make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&Vs[i], &Ws[i])
	}
	// DP[i+1][j] := i個目までの商品のうち重さがj以下になるよう選んだときの価値の最大値
	for i := 0; i < N; i++ {
		for j := 0; j <= W; j++ {
			if Ws[i] <= j {
				// DP[i+1][j] = max(DP[i][j], DP[i][j-Ws[i]]+Vs[i]) これは01ナップザック
				DP[i+1][j] = max(DP[i][j], DP[i+1][j-Ws[i]]+Vs[i]) // これは個数無制限ナップザック
			} else {
				DP[i+1][j] = DP[i][j]
			}
		}
	}
	fmt.Println(DP[N][W])
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
