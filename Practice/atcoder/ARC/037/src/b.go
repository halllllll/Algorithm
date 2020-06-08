// dfs 木の条件 辺が頂点数-1

package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	T := make([][]int, N+1)
	for i := 1; i <= N; i++ {
		T[i] = []int{}
	}
	for i := 0; i < M; i++ {
		var U, V int
		fmt.Scan(&U, &V)
		T[U] = append(T[U], V)
		T[V] = append(T[V], U)
	}
	parent := make([]int, N+1)
	ans := 0
	for i := 1; i <= N; i++ {
		if parent[i] != 0 {
			continue
		}
		parent[i] = i
		queue := []int{i}
		edgeCount := 0
		nodeCoount := 1
		for len(queue) > 0 {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			edgeCount += len(T[cur])
			for _, nex := range T[cur] {
				if parent[nex] == 0 {
					parent[nex] = i
					nodeCoount++
					queue = append(queue, nex)
				}
			}
		}
		edgeCount /= 2
		if nodeCoount-1 == edgeCount {
			ans++
		}
	}
	fmt.Println(ans)
}
