package main

import (
	"fmt"
	"sort"
)

var n int
var a float64
var arr []int
var dp [51][51][2501]int

func main() {
	fmt.Scan(&n, &a)
	arr = make([]int, n)
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		arr[i] = j
	}
	sort.Ints(arr)
	if int(a) < arr[0] {
		fmt.Println(0)
		return
	}
	for i := 0; i < 51; i++ {
		for j := 0; j < 51; j++ {
			for k := 0; k < 2051; k++ {
				dp[i][j][k] = -1
			}
		}
	}
	fmt.Println(rec(0, 0, 0))
}

func rec(i, j, k int) int {
	if dp[i][j][k] >= 0 {
		return dp[i][j][k]
	}
	if i == n {
		if float64(k)/float64(j) == a {
			dp[i][j][k] = 1
			return 1
		} else {
			dp[i][j][k] = 0
			return 0
		}
	}

	ret := rec(i+1, j, k) + rec(i+1, j+1, k+arr[i])
	dp[i][j][k] = ret
	return ret
}
