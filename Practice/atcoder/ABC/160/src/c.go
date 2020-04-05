// 最大長の区間を省く
package main

import "fmt"

func main() {
	var k, n int
	var a []int
	fmt.Scan(&k, &n)
	a = make([]int, n)
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		a[i] = j
	}
	base := k - a[n-1] + a[0]
	for i := 0; i < n-1; i++ {
		base = max(base, a[i+1]-a[i])
	}
	fmt.Println(k - base)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
