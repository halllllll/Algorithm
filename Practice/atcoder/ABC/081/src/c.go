package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	d := make(map[int]int)
	// どの番号があるかは関係がない いくつあるかだけ
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		if _, ok := d[a]; ok {
			d[a]++
		} else {
			d[a] = 1
		}
	}
	numbers, variety := make([]int, 0), len(d)
	for _, value := range d {
		numbers = append(numbers, value)
	}
	sort.Ints(numbers)
	ans := 0
	for k < variety {
		ans += numbers[0]
		numbers = numbers[1:]
		variety--
	}
	fmt.Println(ans)
}
