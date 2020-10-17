// 解説AC 全探索 整数判定はceilを使った -> なんか駄目でした
package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	X, Y := make([]int, N), make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&X[i], &Y[i])
	}
	ans := 0
	for i := 0; i < N; i++ {
		for j := i + 1; j < N; j++ {
			for k := j + 1; k < N; k++ {
				X1, Y1 := X[j]-X[i], Y[j]-Y[i]
				X2, Y2 := X[k]-X[i], Y[k]-Y[i]
				S := abs(abs(X1*Y2) - abs(Y1*X2))
				if S%2.0 == 0 && S != 0 {
					ans++
				}
			}
		}
	}
	fmt.Println(ans)
}

func abs(x int) int {
	if x < 0 {
		x *= -1.0
	}
	return x
}
