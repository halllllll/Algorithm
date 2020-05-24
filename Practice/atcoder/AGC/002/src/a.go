package main

import "fmt"

func main() {
	var A, B int
	fmt.Scan(&A, &B)
	if 0 < A {
		fmt.Println("Positive")
	} else if A <= 0 && 0 <= B {
		fmt.Println("Zero")
	} else {
		if abs(B-A+1)%2 == 0 {
			fmt.Println("Positive")
		} else {
			fmt.Println("Negative")
		}
	}
}

func abs(a int) int {
	if a < 0 {
		a *= -1
	}
	return a
}
