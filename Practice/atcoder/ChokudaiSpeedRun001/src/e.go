package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if V == 1 {
			fmt.Println(i + 1)
			return
		}
	}
}
