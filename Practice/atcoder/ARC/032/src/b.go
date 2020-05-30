// 木の数-1な気がする unionfindでいいか？
// 意味不明なWA
// なんかしらんけど最後にもっかい無理やりrootしたらうまくいった
package main

import "fmt"

var parent []int

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	parent = make([]int, N)
	for i := 0; i < N; i++ {
		parent[i] = i
	}
	for i := 0; i < M; i++ {
		var A, B int
		fmt.Scan(&A, &B)
		if A > B {
			A, B = B, A
		}
		union(A-1, B-1)
	}
	used := make(map[int]bool)
	for i := 0; i < N; i++ {
		used[root(i)] = true
	}
	fmt.Println(len(used) - 1)
}

func root(x int) int {
	if x == parent[x] {
		return x
	}
	y := root(parent[x])
	parent[x] = y
	return parent[x]
}

func union(a, b int) {
	ra, rb := root(a), root(b)
	if ra != rb {
		parent[rb] = ra
	}
}
