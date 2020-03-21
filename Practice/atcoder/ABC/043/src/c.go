package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	ans := 1<<32 - 1
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		var m int
		fmt.Scan(&m)
		arr[i] = m
	}
	for i := -100; i <= 100; i++ {
		tmp := 0
		for _, ai := range arr {
			tmp += (i - ai) * (i - ai)
		}
		ans = min(ans, tmp)
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
