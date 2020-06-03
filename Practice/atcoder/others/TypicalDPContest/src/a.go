// できるだけループを使おうねキャンペーン
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	P := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		P[i] = V
	}
	DP := make([][]int, N+100)
	for i := 0; i < N+100; i++ {
		DP[i] = make([]int, 100*100+100)
		for j := 0; j < len(DP[i]); j++ {
			DP[i][j] = 0
		}
	}
	DP[0][0] = 1
	for i := 0; i < N; i++ {
		for j := 0; j <= 100*100; j++ {
			if j >= P[i] {
				DP[i+1][j] = DP[i][j] | DP[i][j-P[i]]
			} else {
				DP[i+1][j] = DP[i][j]
			}
		}
	}
	ans := 0
	for j := 0; j <= 100*100; j++ {
		ans += DP[N][j]
	}
	fmt.Println(ans)
}
