// おもむろにbit全探索をググる
// 結局実装わかんなくて解説をパクっただけ、理解まったくしてないよね君

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	F := make([][]int, N)
	for i := 0; i < N; i++ {
		F[i] = make([]int, 10)
		for j := 0; j < 10; j++ {
			var k int
			fmt.Scan(&k)
			F[i][j] = k
		}
	}
	P := make([][]int, N)
	for i := 0; i < N; i++ {
		P[i] = make([]int, 11)
		for j := 0; j < 11; j++ {
			var k int
			fmt.Scan(&k)
			P[i][j] = k
		}
	}
	ans := -(1 << uint64(36))
	for bit := 1; bit < (1 << uint64(10)); bit++ {
		tmp := 0
		for i := 0; i < N; i++ {
			c := 0
			for j := 0; j < 10; j++ {
				if (bit>>uint64(j))&1 == 1 && F[i][j] == 1 {
					c += 1
				}
			}
			tmp += P[i][c]
		}
		ans = max(ans, tmp)
	}
	fmt.Println(ans)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
