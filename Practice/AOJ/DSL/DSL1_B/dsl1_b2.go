package main

import "fmt"

func main() {
	var N, Q int
	fmt.Scan(&N, &Q)
	parent := make([]int, N)
	weight := make([]int, N)
	for i := 0; i < N; i++ {
		parent[i] = i
	}

	var root func(i int) int
	var union func(i, j, k int)
	root = func(x int) int {
		if x == parent[x] {
			return x
		}
		y := root(parent[x])
		weight[x] += weight[parent[x]]
		parent[x] = y
		return y
	}
	union = func(a, b, w int) {
		ra, rb := root(a), root(b)
		if ra != rb {
			if b == rb {
				// w = aからaの根+aの根からbの根
				weight[ra] = w - weight[a]
			} else {
				// w = aからaの根+aの根からbの根+bの根からb
				// w = aからaの根+aの根からbの根-bからbの根
				weight[ra] = w - (weight[a] - weight[b])
			}
			parent[ra] = rb // これポイント
		}
	}

	for i := 0; i < Q; i++ {
		var query int
		fmt.Scan(&query)
		if query == 0 {
			var x, y, z int
			fmt.Scan(&x, &y, &z)
			union(x, y, z)
		} else {
			var x, y int
			fmt.Scan(&x, &y)
			if root(x) != root(y) {
				fmt.Println("?")
			} else {
				fmt.Println(weight[x] - weight[y])
			}
		}
	}
}
