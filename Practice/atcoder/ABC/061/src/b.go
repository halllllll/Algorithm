package main

import (
	"fmt"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	d := make(map[int]int)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		if _, ok := d[a-1]; ok {
			d[a-1]++
		} else {
			d[a-1] = 1
		}
		if _, ok := d[b-1]; ok {
			d[b-1]++
		} else {
			d[b-1] = 1
		}
	}
	for i := 0; i < n; i++ {
		fmt.Println(d[i])
	}
}
