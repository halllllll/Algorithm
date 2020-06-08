// ノードからDFSした葉が1を返す
// 混乱しがちで個人的に良い問題
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	member := make([][]int, N+1)
	for i := 0; i <= N; i++ {
		member[i] = []int{}
	}
	member[0] = append(member[0], -1)

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
		retMax, retMin := 0, int(1e17)
		for _, nex := range member[i] {
			retMax = max(retMax, dfs(nex))
			retMin = min(retMin, dfs(nex))
		}
		return 1 + retMax + retMin
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
