package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	MOD := int(1e4) + 7
	if N <= 2 {
		fmt.Println(0)
	} else if N <= 4 {
		fmt.Println(1)
	} else {
		a, b, c := 0, 1, 1
		N -= 4
		for N > 0 {
			N--
			a, b, c = b, c, a+b+c
			c %= MOD
		}
		fmt.Println(c)
	}
}
