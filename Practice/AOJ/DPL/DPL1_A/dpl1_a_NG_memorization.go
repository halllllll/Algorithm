// ループでDPつくるのぜんぜんわからん定期
// かといってメモ化DPでやったらMLEなった

package main

import (
	"fmt"
)

var N, M int
var C []int
var memo map[[2]int]int

func main() {
	fmt.Scan(&N, &M)
	C = make([]int, M)
	memo = make(map[[2]int]int)
	for i := 0; i < M; i++ {
		fmt.Scan(&C[i])
	}
	ans := rec(N, 0)
	fmt.Println(ans)
}

func rec(sum, count int) int {
	if _, ok := memo[[2]int{sum, count}]; ok {
		return memo[[2]int{sum, count}]
	}
	if sum == 0 {
		return count
	}
	ret := int(1e18)
	for i := 0; i < M; i++ {
		if sum-C[i] >= 0 {
			ret = min(ret, rec(sum-C[i], count+1))
		}
	}
	memo[[2]int{sum, count}] = ret
	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
