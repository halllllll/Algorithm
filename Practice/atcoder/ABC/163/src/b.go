package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	S := 0
	for i := 0; i < M; i++ {
		var j int
		fmt.Scan(&j)
		S += j
	}
	if N-S >= 0 {
		fmt.Println(N - S)
	} else {
		fmt.Println(-1)
	}
}
