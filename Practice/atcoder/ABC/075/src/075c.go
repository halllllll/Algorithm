// 1こずつ無視したとしたときの全探索
package main

import "fmt"

type Edge struct {
	A, B int
}

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	E := make([]Edge, M)
	for i := 0; i < M; i++ {
		var A, B int
		fmt.Scan(&A, &B)
		E[i] = Edge{A: A, B: B}
	}
	ans := 0
	for i := 0; i < M; i++ {
		T := make([][]int, N+1)
		for j := 0; j < N+1; j++ {
			T[j] = []int{}
		}
		for j := 0; j < M; j++ {
			if i == j {
				continue
			}
			T[E[j].A] = append(T[E[j].A], E[j].B)
			T[E[j].B] = append(T[E[j].B], E[j].A)
		}
		used := make(map[int]bool)
		queue := []int{1}
		used[1] = true
		for len(queue) > 0 {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			for _, nex := range T[cur] {
				if _, ok := used[nex]; !ok {
					used[nex] = true
					queue = append(queue, nex)
				}
			}
		}
		if len(used) != N {
			ans++
		}
	}
	fmt.Println(ans)
}
