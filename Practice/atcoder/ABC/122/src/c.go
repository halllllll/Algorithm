// なぜかREになるが意味不明

package main

import "fmt"

func main() {
	var N, Q int
	fmt.Scan(&N, &Q)
	var S string
	fmt.Scan(&S)
	SS := make([]string, len(S))
	for i, c := range []rune(S) {
		SS[i] = string(c)
	}
	ruiseki := make([]int, N+1)
	for i := 0; i < len(SS)-1; i++ {
		if SS[i] == "A" && SS[i+1] == "C" {
			ruiseki[i+1]++
		}
	}
	//             ↓ ????????????????????????
	for i := 1; i <= N; i++ {
		ruiseki[i] += ruiseki[i-1]
	}
	for i := 0; i < Q; i++ {
		var L, R int
		fmt.Scan(&L, &R)
		L, R = L-1, R-1
		fmt.Println(ruiseki[R] - ruiseki[L])
	}
}
