// 上下左右まとめられる 最初組み合わせかと思って死んでた
package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	fmt.Scan(&S)
	LS, RS := strings.Count(S, "L"), strings.Count(S, "R")
	US, DS := strings.Count(S, "U"), strings.Count(S, "D")
	X := len(S) - (LS + RS + US + DS)
	var T int
	fmt.Scan(&T)
	if X == 0 {
		fmt.Println(abs(LS-RS) + abs(US-DS))
	} else {
		if T == 1 {
			fmt.Println(abs(LS-RS) + abs(US-DS) + X)
		} else {
			if (abs(LS-RS) + abs(US-DS)) > X {
				fmt.Println((abs(LS-RS) + abs(US-DS)) - X)
			} else {
				fmt.Println((X - (abs(LS-RS) + abs(US-DS))) % 2)
			}
		}
	}
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}
