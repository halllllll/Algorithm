// コイン問題DPでやった

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	DP := make([]int, N+101010)
	for i := 1; i < len(DP); i++ {
		DP[i] = i // 1円で支払う気持ち
	}
	for i := 1; i <= N; i++ {
		for c := 6; c <= N; c *= 6 {
			if i >= c {
				DP[i] = min(DP[i], DP[i-c]+1)
			}
		}
		for c := 9; c <= N; c *= 9 {
			if i >= c {
				DP[i] = min(DP[i], DP[i-c]+1)
			}
		}
	}
	fmt.Println(DP[N])
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
