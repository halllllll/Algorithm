// 貪欲でいいんじゃないか
// まだ解いてないです 2020/05/24
package main

import "fmt"

var N, L int

func main() {
	fmt.Scan(&N, &L)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	Ruiseki := make([]int, N)
	Ruiseki[0] = A[0]
	for i := 1; i < N; i++ {
		Ruiseki[i] = Ruiseki[i-1] + A[i]
	}
	fmt.Println(Ruiseki)
}
