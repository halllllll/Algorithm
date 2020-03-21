package main

import (
	"fmt"
)

var h, w int

func main() {
	fmt.Scan(&h, &w)
	if h == 1 || w == 1 {
		fmt.Println(max(h, w) - 1)
	} else if h == 2 || w == 2 {
		fmt.Println(max(h, w) + (max(h, w)-1)*2)
	} else {
		fmt.Println((h-1)*w + (w-1)*h)
	}
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
