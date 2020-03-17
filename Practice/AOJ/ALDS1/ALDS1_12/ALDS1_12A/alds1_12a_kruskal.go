package main

import (
	"fmt"
	"sort"
)

type Edge struct {
	a, b, cost int
}

func main() {
	var n int
	fmt.Scan(&n)
	edges := make([]Edge, 0)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			var t int
			fmt.Scan(&t)
			if t >= 0 {
				e := Edge{a: i, b: j, cost: t}
				edges = append(edges, e)
			}
		}
	}

	// AOJのgolangのバージョンは新しいと思うので構造体のフィールドをキーにするタイプのソートが簡単にできるはず(1.8以降のやつだっけ)
	sort.Slice(edges, func(i, j int) bool {
		return edges[i].cost < edges[j].cost
	})

	// unionfindを使って使ってないエッジを取り込んでいくが、その過程で（どうせ全域木になるのが前提なので）答えを加算していける
	parents := make([]int, n)
	for i := 0; i < n; i++ {
		parents[i] = i
	}
	ans := 0
	for _, e := range edges {
		if find(e.a, e.b, parents) {
			union(e.a, e.b, parents)
			ans += e.cost
		}
	}
	fmt.Println(ans)
}

func union(a, b int, arr []int) {
	ra, rb := root(a, arr), root(b, arr)
	arr[rb] = ra
}

func root(a int, arr []int) int {
	if a == arr[a] {
		return a
	}
	b := root(arr[a], arr)
	arr[a] = b
	return b
}

func find(a, b int, arr []int) bool {
	return root(a, arr) != root(b, arr)
}
