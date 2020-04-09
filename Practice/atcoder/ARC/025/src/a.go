package main

import "fmt"

func main() {
	d, j := make([]int, 7), make([]int, 7)
	for i := 0; i < 7; i++ {
		var di int
		fmt.Scan(&di)
		d[i] = di
	}
	for i := 0; i < 7; i++ {
		var ji int
		fmt.Scan(&ji)
		j[i] = ji
	}
	ans := 0
	for i := 0; i < 7; i++ {
		if d[i] < j[i] {
			ans += j[i]
		} else {
			ans += d[i]
		}
	}
	fmt.Println(ans)
}
