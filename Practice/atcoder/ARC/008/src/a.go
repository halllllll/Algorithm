package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := n * 15
	b := (n/10)*100 + (n%10)*15
	c := (n/10 + 1) * 100
	ans := min(a, min(b, c))
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
