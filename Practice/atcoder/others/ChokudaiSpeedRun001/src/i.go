// すべて正の整数なのでしゃくとりでいいわけよ
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	r := 0
	ans := 0
	tmp := 0
	for l := 0; l < N; l++ {
		for r < N && tmp < N {
			tmp += A[r]
			r++
		}
		if tmp == N {
			ans++
		}
		if l == r {
			r++
		} else {
			tmp -= A[l]
		}
	}
	fmt.Println(ans)
}
