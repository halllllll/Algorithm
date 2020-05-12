package main

import "fmt"

func main() {
	var N, A, B int
	fmt.Scan(&N, &A, &B)
	fmt.Println(max(0, A+(B*(N-1))-(B+(A*(N-1)))+1))
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
