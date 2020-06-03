package main

import (
	"fmt"
)

var n, m int
var a map[int]int

func main() {
	a = make(map[int]int)
	fmt.Scan(&n, &m)
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		if _, ok := a[j]; ok {
			a[j] += 1
		} else {
			a[j] = 1
		}
	}
	for k, v := range a {
		if n/2 < v {
			fmt.Println(k)
			return
		}
	}
	fmt.Println("?")
}
