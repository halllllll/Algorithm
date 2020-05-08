// 無能
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := []string{}
	for i := 0; i < N; i++ {
		var V string
		fmt.Scan(&V)
		for _, c := range []rune(V) {
			A = append(A, string(c))
		}
	}

	MOD := 1000000007
	cur := 0
	for i := 0; i < len(A); i++ {
		x, _ := strconv.Atoi(A[i])
		cur = 10*cur + x
		cur %= MOD
	}
	fmt.Println(cur)
}
