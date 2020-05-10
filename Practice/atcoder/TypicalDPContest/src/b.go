package main

import "fmt"

var A, B int
var X, Y []int
var M [][]int

func main() {
	fmt.Scan(&A, &B)
	X, Y = make([]int, A), make([]int, B)
	M = make([][]int, A+100)
	for i := 0; i < A; i++ {
		var V int
		fmt.Scan(&V)
		X[i] = V
	}
	for i := 0; i < B; i++ {
		var V int
		fmt.Scan(&V)
		Y[i] = V
	}
	for i := 0; i < len(M); i++ {
		M[i] = make([]int, B+100)
	}
	fmt.Println(rec(0, 0))
}

func rec(i, j int) int {
	if i+j == A+B {
		return 0
	}
	if M[i][j] > 0 {
		return M[i][j]
	}
	ret := -100000000000
	if (i+j)%2 == 0 {
		// すぬけのターン
		if i < A && j < B {
			ret = max(ret, max(rec(i+1, j)+X[i], rec(i, j+1)+Y[j]))
		} else if i == A {
			ret = max(ret, rec(i, j+1)+Y[j])
		} else if j == B {
			ret = max(ret, rec(i+1, j)+X[i])
		} else {
			fmt.Println("お？？？？？？？？")
		}
	} else {
		// すめけのターン
		// 「得点が得られない」という発想...
		if i < A && j < B {
			ret = min(rec(i+1, j), rec(i, j+1))
		} else if i == A {
			ret = rec(i, j+1)
		} else if j == B {
			ret = rec(i+1, j)
		} else {
			fmt.Println("え？？？？？？")
		}
	}
	M[i][j] = ret
	return ret
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
