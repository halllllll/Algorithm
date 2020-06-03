package main

import (
	"fmt"
	"sort"
)
var n, m int
var a []int
func main() {
	fmt.Scan(&n, &m)
	a = make([]int, m+100)
	max_n, max_i := 0, 0
	for i:=0; i<n; i++{
		var j int
		fmt.Scan(&j)
		a[j]++
		if a[j] > max_n{
			max_n = a[j]
			max_i = j
		}
	}
	sort.Ints(a)
	if (m > 1 && a[len(a)-1] == a[len(a)-2]) || max_n <= n/2{
		fmt.Println("?")
	}else{
		fmt.Println(max_i)
	}

}
