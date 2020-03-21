// ふつうにソートでやるとTLEなった これはPriority Queueで叩くやつだった

package main

import (
	"fmt"
	"sort"
)

type Edge struct {
	x, y, cost int
}

var parents []int
var edges []Edge

func main() {
	var v, e int
	fmt.Scan(&v, &e)
	parents = make([]int, v)
	edges = make([]Edge, e)
	for i := 0; i < v; i++ {
		parents[i] = i
	}
	for i := 0; i < e; i++ {
		var s, t, w int
		fmt.Scan(&s, &t, &w)
		edges[i] = Edge{x: s, y: t, cost: w}
	}
	sort.Slice(edges, func(i, j int) bool {
		return edges[i].cost < edges[j].cost
	})
	ans := 0
	for _, e := range edges {
		if !same(e.x, e.y) {
			union(e.x, e.y)
			ans += e.cost
		}
	}
	fmt.Println(ans)
}

func root(x int) int {
	if x == parents[x] {
		return x
	}
	y := root(parents[x])
	parents[x] = y
	return y
}

func same(a, b int) bool {
	return root(a) == root(b)
}

func union(a, b int) {
	ra, rb := root(a), root(b)
	parents[ra] = rb
}
