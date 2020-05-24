// 最大の木の大きさじゃないの？ -> ちがうみたいです せっかくunion findやったのに（誤読
package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	G := make([][]bool, N+1)
	for i := 0; i < N; i++ {
		G[i] = make([]bool, N+1)
	}
	for i := 0; i < M; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		G[x][y] = true
		G[y][x] = true
	}

	for bit := 0; bit < (1 << N); bit++ {
		friends := []int{}
		for i := 0; i < N; i++ {
			if bit&(1<<i) == 1 {
				friends = append(friends, i+1)
			}
		}
		// 組み合わせここで計算するの？？？？？？
		for i := 0; i < len(friends); i++ {
			for j := 0; j < len(friends); j++ {
				
			}
		}
	}
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
