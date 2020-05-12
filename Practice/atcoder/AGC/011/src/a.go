// にぶたんの臭いがしたけどぜんぜん違ったわ 1時間くらい無駄にした
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N, C, K int
	fmt.Scan(&N, &C, &K)
	T := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		T[i] = V
	}
	sort.Ints(T)
	bus := 1
	currentTime := T[0]
	limitTIme := currentTime + K
	passenger := 0
	arr := []int{}
	for _, t := range T {
		if passenger+1 > C || t > limitTIme {
			arr = []int{t}
			bus++
			passenger = 1
			currentTime = t
			limitTIme = currentTime + K
		} else {
			passenger++
			arr = append(arr, t)
		}
	}
	fmt.Println(bus)
}
