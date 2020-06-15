package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	if N == 0 || N == 1 {
		fmt.Println(1)
		return
	}
	idx := 2
	a, b := 1, 1
	for idx <= N {
		a, b = b, a+b
		idx++
	}
	fmt.Println(b)
}
