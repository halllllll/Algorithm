package main

import "fmt"

func main() {
	var A, B, C int
	fmt.Scan(&A, &B, &C)
	if (A < C) && (C < B) || (A > C) && (C > B) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
