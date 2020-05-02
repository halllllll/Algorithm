package main

import "fmt"

func main() {
	var A, B, C, D int
	fmt.Scan(&A, &B, &C, &D)
	countOfdeathA := 0
	if A%D == 0 {
		countOfdeathA = A / D
	} else {
		countOfdeathA = A/D + 1
	}
	if C-B*countOfdeathA > 0 {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}
}
