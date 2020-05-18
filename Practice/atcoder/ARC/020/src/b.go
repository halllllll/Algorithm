// 脳死で全探索します おわり
package main

import "fmt"

func main() {
	var N, C int
	fmt.Scan(&N, &C)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	ans := int(1e10)
	for i := 1; i <= 10; i++ {
		for j := 1; j <= 10; j++ {
			if i == j {
				continue
			}
			tmp := 0
			for k := 0; k < N; k++ {
				if k%2 == 0 {
					if A[k] != i {
						tmp++
					}
				} else {
					if A[k] != j {
						tmp++
					}
				}
			}
			ans = min(ans, tmp)
		}
	}
	fmt.Println(ans * C)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
