// きりみんちゃんの配信からきました
package main

import "fmt"

var n, m, x int

func main() {
	fmt.Scan(&n, &m, &x)
	left, right := 0, 0
	for i := 0; i < m; i++ {
		var j int
		fmt.Scan(&j)
		if j < x {
			left += 1
		} else {
			right += 1
		}
	}
	if left < right {
		fmt.Println(left)
	} else {
		fmt.Println(right)
	}
}
