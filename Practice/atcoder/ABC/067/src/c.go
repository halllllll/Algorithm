// https://kenkoooo.com/atcoder/#/contest/show/a9a7a4e2-047d-4784-8e13-668951991a1d からきました
// sumから引いていって最小値を更新
package main

import "fmt"

var n int
var a []int

func main() {
	fmt.Scan(&n)
	a = make([]int, n)
	y := 0
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		a[i] = j
		y += j
	}
	if n == 2 {
		fmt.Println(abs(a[0] - a[1]))
		return
	}
	ans := 10000000000
	x := a[0]
	y -= x
	for i := 1; i < n-1; i++ {
		ans = min(ans, abs(x-y))
		x += a[i]
		y -= a[i]
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -1 * a
}
