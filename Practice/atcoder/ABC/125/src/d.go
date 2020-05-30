// 問題文読んでないけど負数が奇数の場合は両端どっちかで偶数の場合はなんとなく全部正にできそう
// """0""" の存在を忘れていた...
// 意味不明なことにWA
// アホだった なーにが「両端どっちか」じゃボケが 最小値にすることが可能
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	S := 0
	minus := 0
	zero := false
	minn := int(1e10)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if V == 0 {
			zero = true
		} else {
			minn = min(minn, abs(V))
		}
		A[i] = abs(V)
		S += abs(V)
		if V < 0 {
			minus++
		}
	}
	if zero {
		fmt.Println(S)
	} else if minus%2 == 0 {
		fmt.Println(S)
	} else {
		fmt.Println(S - minn*2)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}
