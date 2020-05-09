package main

import "fmt"

func main() {
	var N, Q int
	fmt.Scan(&N, &Q)
	T := make([][]string, N)
	for i := 0; i < N; i++ {
		T[i] = make([]string, N)
		for j := 0; j < N; j++ {
			T[i][j] = "N"
		}
	}
	for i := 0; i < Q; i++ {
		var Q int
		fmt.Scan(&Q)
		if Q == 1 {
			var a, b int
			fmt.Scan(&a, &b)
			T[a-1][b-1] = "Y"
		} else if Q == 2 {
			var a int
			fmt.Scan(&a)
			// めんどくせぇ 全探索だ
			for j := 0; j < N; j++ {
				if T[j][a-1] == "Y" {
					T[a-1][j] = "Y"
				}
			}
		} else if Q == 3 {
			var a int
			fmt.Scan(&a)
			ff := []int{}
			for j := 0; j < N; j++ {
				if T[a-1][j] == "Y" {
					ff = append(ff, j)
				}
			}
			for _, fff := range ff {
				for j := 0; j < N; j++ {
					if T[fff][j] == "Y" {
						T[a-1][j] = "Y"
					}
				}
			}
		}
	}
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i == j && T[i][j] == "Y" {
				fmt.Print("N")
			} else {
				fmt.Print(T[i][j])
			}
		}
		fmt.Println()
	}
}
