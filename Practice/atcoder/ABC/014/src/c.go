package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([]int, 1000010)
	for i := 0; i < n; i++ {
		var a, b int
		fmt.Scan(&a)
		fmt.Scan(&b)
		arr[a] += 1
		arr[b+1] -= 1
	}
	for i, _ := range arr {
		if i == 0 {
			continue
		}
		arr[i] += arr[i-1]
	}
	ans := 0
	for _, a := range arr {
		if a > ans {
			ans = a
		}
	}
	fmt.Println(ans)
}
