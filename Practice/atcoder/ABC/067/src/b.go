package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		numbers[i] = a
	}
	sort.Sort(sort.Reverse(sort.IntSlice(numbers)))
	// goに#slice.sum()など存在しない
	ans := 0
	for _, v := range numbers[:k] {
		ans += v
	}
	fmt.Println(ans)
}
