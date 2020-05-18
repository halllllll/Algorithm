// AGCは質が高くていいな〜〜
// 枯渇しない限りは拡散できる
// 最初1-indexedにしてたのに0に赤を置いてて無限時間バグった

package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	Balls := make([]int, N+1)
	PossibilityRed := make([]bool, N+1)
	for i := 1; i <= N; i++ {
		Balls[i] = 1
		PossibilityRed[i] = false // いらんけど
	}
	PossibilityRed[1] = true
	for i := 0; i < M; i++ {
		var A, B int
		fmt.Scan(&A, &B)
		if Balls[A] == 0 {
			continue // あるかどうかしらんけど
		}
		if PossibilityRed[A] {
			PossibilityRed[B] = true
			if Balls[A] == 1 {
				PossibilityRed[A] = false
			}
		}
		Balls[A]--
		Balls[B]++
	}
	ans := 0
	for _, p := range PossibilityRed {
		if p {
			ans++
		}
	}
	fmt.Println(ans)
}
