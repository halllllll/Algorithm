// もしかしてすべてのxorが0になれば大丈夫説
// 理屈はわからんがなんかしらんけど通った。。。。
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	xor := A[0]
	for i := 1; i < N; i++ {
		xor = xor ^ A[i]
	}
	if xor == 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
