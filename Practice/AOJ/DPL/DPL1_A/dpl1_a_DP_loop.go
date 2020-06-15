// 正直なんでそうなるのかわかってないです

package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	C := make([]int, M)
	for i := 0; i < M; i++ {
		fmt.Scan(&C[i])
	}
	INF := int(1e18)
	// DP[i+1] := i円を達成するのに必要なコインの最小の枚数
	DP := make([]int, N+10000) // 貰うDPのために余裕をもっておく
	for i := 0; i < len(DP); i++ {
		DP[i] = INF
	}
	DP[0] = 0 // 0円を達成するには0枚でいい
	// これは配るDP
	// for i := 0; i <= N; i++ {
	// 	for j := 0; j < M; j++ {
	// 		if C[j]+i <= N {
	// 			DP[i+C[j]] = min(DP[i]+1, DP[i+C[j]])
	// 		}
	// 	}
	// }
	// これは貰うDP
	for i := 1; i <= N; i++ {
		for j := 0; j < M; j++ {
			// if C[j]+i <= N {
			if i >= C[j] {
				DP[i] = min(DP[i], DP[i-C[j]]+1)
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
