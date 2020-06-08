package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	member := make([][]int, N+1)
	for i := 0; i <= N; i++ {
		member[i] = []int{}
	}
	for i := 1; i < N; i++ {
		var B int
		fmt.Scan(&B)
		member[B] = append(member[B], i+1)
	}

	var dfs func(i int) int
	dfs = func(i int) int {
		if len(member[i]) == 0 {
			return 1
		}
		minn, maxn := int(1e10), 0
		for _, m := range member[i] {
			x := dfs(m)
			minn = min(minn, x)
			maxn = max(maxn, x)
		}
		return minn + maxn + 1
	}
	fmt.Println(dfs(1))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
