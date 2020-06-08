// 前やったのを覚えていたので虚無

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var H, W, N int
	fmt.Scan(&H, &W, &N)
	A := make([]int, N)
	T := make([][]string, H)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	for i := 0; i < H; i++ {
		T[i] = make([]string, W)
	}
	idx := 0
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			k := j
			if i%2 == 1 {
				k = W - j - 1
			}
			T[i][k] = strconv.Itoa(idx + 1)
			A[idx]--
			if A[idx] == 0 {
				idx++
			}
		}
	}
	for _, t := range T {
		fmt.Println(strings.Join(t, " "))
	}
}
