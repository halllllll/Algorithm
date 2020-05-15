// 自分より小さい分をすべて喰って2倍しても自分よりひとつ大きいのに届かなければ終了
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	B := make([]int, N)

	sort.Ints(A)
	B[0] = A[0]
	for i := 1; i < N; i++ {
		B[i] = A[i] + B[i-1]
	}
	ans := 1
	for i := N - 2; i >= 0; i-- {
		if B[i]*2 >= A[i+1] {
			ans++
		} else {
			break
		}
	}
	fmt.Println(ans)
}
