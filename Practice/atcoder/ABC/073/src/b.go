package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	ans := 0
	for i := 0; i < n; i++ {
		var l, r int
		fmt.Scan(&l, &r)
		ans += r - l + 1
	}
	fmt.Println(ans)
}
