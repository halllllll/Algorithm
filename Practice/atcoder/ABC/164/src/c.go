package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	T := make(map[string]bool)
	ANS := 0
	for i := 0; i < N; i++ {
		var S string
		fmt.Scan(&S)
		if _, ok := T[S]; !ok {
			ANS += 1
			T[S] = true
		}
	}
	fmt.Println(ANS)
}
