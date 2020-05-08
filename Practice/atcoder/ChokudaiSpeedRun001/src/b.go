package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	ans := 0
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		ans += V
	}
	fmt.Println(ans)
}
