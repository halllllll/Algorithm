package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	S := 0
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
		S += A[i]
	}
	if S%N != 0 {
		fmt.Println(-1)
		return
	}
	T := S / N
	ans := 0
	cur := 0
	length := 0
	for i := 0; i < N; i++ {
		cur += A[i]
		if cur%(length+1) == 0 && cur/(length+1) == T {
			length = 0
			cur = 0
		} else {
			ans++
			length++
		}
	}
	fmt.Println(ans)
}
