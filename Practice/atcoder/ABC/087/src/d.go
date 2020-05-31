// weighted union findわかりません

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Node struct {
	to, cost int
}

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()

	N, M := nextInt(), nextInt()
	T := make([][]Node, N+1)
	for i := 0; i <= N; i++ {
		T[i] = []Node{}
	}
	for i := 0; i < M; i++ {
		L, R, D := nextInt(), nextInt(), nextInt()
		T[L] = append(T[L], Node{to: R, cost: D})
		T[R] = append(T[R], Node{to: L, cost: -D})
	}

	passed := make([]bool, N+1)
	dist := make([]int, N+1)

	// nodeを出発して通りがかりのcostをもちつつ全探索
	var dfs func(i, j int) bool
	dfs = func(node, d int) bool {
		if passed[node] {
			if dist[node] != d {
				return false
			} else {
				return true
			}
		}
		// 未踏
		passed[node] = true
		dist[node] = d
		for i, nexNode := range T[node] {
			if !dfs(nexNode.to, d+T[node][i].cost) {
				return false
			}
		}
		return true
	}

	// 1orderにしてるんでね
	for i := 1; i <= N; i++ {
		if passed[i] {
			continue
		}
		if !dfs(i, 0) {
			fmt.Fprintln(out, "No")
			return
		}
	}
	fmt.Fprintln(out, "Yes")
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}
