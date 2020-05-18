package main

import "fmt"

var T [][]bool
var N, M int

func main() {
	fmt.Scan(&N, &M)
	T = make([][]bool, N+1)
	for i := 1; i <= N; i++ {
		T[i] = make([]bool, N+1)
	}
	for i := 0; i < M; i++ {
		var A, B int
		fmt.Scan(&A, &B)
		T[A][B] = true
		T[B][A] = true
	}
	for i := 1; i <= N; i++ {
		fmt.Println(rec(i))
	}
}

func rec(user int) (ret int) {
	used := make(map[int]bool)
	for i := 1; i <= N; i++ {
		if !T[user][i] {
			continue
		}
		for j := 1; j <= N; j++ {
			if T[i][j] && !T[user][j] && user != j {
				used[j] = true
			}
		}
	}

	// fmt.Printf("%d の友人の友人: %v\n", user, used)

	for k, _ := range used {
		if user != k {
			ret++
		}
	}
	return
}
