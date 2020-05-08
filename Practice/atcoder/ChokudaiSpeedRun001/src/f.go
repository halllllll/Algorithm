package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	ans := 0
	cur := -1
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if cur < V {
			ans += 1
			cur = V
		}
	}
	fmt.Println(ans)
}
