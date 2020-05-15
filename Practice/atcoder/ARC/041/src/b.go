package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	T := make([][]int, N)
	A := make([][]int, N)
	for i := 0; i < N; i++ {
		var S string
		fmt.Scan(&S)
		T[i] = make([]int, M)
		A[i] = make([]int, M)
		for j, c := range []rune(S) {
			x, _ := strconv.Atoi(string(c))
			T[i][j] = x
		}
	}
	for i := 1; i < N-1; i++ {
		for j := 1; j < M-1; j++ {
			for T[i-1][j] >= 1 && T[i][j+1] >= 1 && T[i+1][j] >= 1 && T[i][j-1] >= 1 {
				A[i][j]++
				T[i-1][j]--
				T[i][j+1]--
				T[i+1][j]--
				T[i][j-1]--
			}
		}
	}
	for _, a := range A {
		sa := make([]string, M)
		for j, c := range a {
			cc := strconv.Itoa(c)
			sa[j] = cc
		}
		fmt.Println(strings.Join(sa, ""))
	}
}
