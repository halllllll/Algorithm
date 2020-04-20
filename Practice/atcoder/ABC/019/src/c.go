// なんや 2で割り切れるだけ割ればええんか？
// ぜんぜんちがうわ 任意のxだから2xいれたら4xなる
// 2で割り切れるだけ割り切った数か
package main

import (
	"fmt"
)

func main() {
	var N int
	D := make(map[int]bool)
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	// reverseでけへん
	for i := 0; i < N; i++ {
		for ; A[i]%2 == 0; A[i] /= 2 {
			continue
		}
		D[A[i]] = true
	}
	fmt.Println(len(D))
}
