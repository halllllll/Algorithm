// i-1,iをみて、越えたらiから優先的に取る（次も使えるので）
package main

import "fmt"

func main() {
	var N, X int
	fmt.Scan(&N, &X)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	ans := 0
	for i := 1; i < N; i++ {
		if A[i]+A[i-1] > X {
			surplus := A[i] + A[i-1] - X
			ans += surplus
			A[i] -= surplus
			// A[i-1]は二度と使わんのでどうでもいい
			if A[i] < 0 {
				A[i] = 0
			}
		}
	}
	fmt.Println(ans)
}
