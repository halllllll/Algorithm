package main

import "fmt"

var n, m int
var arr []int
var par []int

func main() {
	fmt.Scan(&n, &m)
	arr = make([]int, n)
	par = make([]int, n)
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		arr[i] = j - 1
		par[i] = i
	}
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		union(a-1, b-1)
	}
	ans := 0
	for i := 0; i < n; i++ {
		ra, rb := root(i), root(arr[i])
		if ra == rb {
			ans += 1
		}
	}
	fmt.Println(ans)
}

func root(x int) int {
	if x == par[x] {
		return x
	}
	xx := root(par[x])
	par[x] = xx
	return xx
}

func union(a, b int) {
	if a > b {
		a, b = b, a
	}
	ra, rb := root(a), root(b)
	if ra != rb {
		par[ra] = rb
	}
}
