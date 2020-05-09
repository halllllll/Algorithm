package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	T := make([]int, N+1)
	ans1 := -1
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if T[V] == 0 {
			T[V] = i + 1
		} else {
			ans1 = V
		}
	}
	if ans1 == -1 {
		fmt.Println("Correct")
	} else {
		from := 0
		for i := 1; i < N+1; i++ {
			if T[i] == 0 {
				from = i
			}
		}
		fmt.Println(ans1, from)
	}
}
