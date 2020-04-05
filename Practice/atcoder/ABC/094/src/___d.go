// きりみんちゃんの配信からきました
// Cのほうが難しくない？
// できるだけN/2に近いほうがでかくなるのは自明
package main

import (
	"fmt"
	"sort"
)

var n int

func main() {
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		a[i] = j
	}
	sort.Ints(a)
	mid, large := a[(n-1)/2], a[n-1]
	fmt.Println(large, mid)
}
