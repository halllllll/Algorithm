// ダイクストラ典型か？N的にワ―シャルフロイドでもいけそう
// と思ったら同じ道を通って戻れないやつだった
// つまり1を含む閉路のうち最小コストを求める感じになる
// じゃBFSでいいっすね
// まだやってないです

package main

import "fmt"

type Grid struct {
	Idx, Cost int
}

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	T := make([][]int, N)
	for i := 0; i < N; i++ {
		T[i] = make([]int, N)
	}
	for i := 0; i < M; i++ {
		var U, V, L int
		fmt.Scan(&U, &V, &L)
		U, V = U-1, V-1
		T[U][V], T[V][U] = V, V
	}
	used := make([]bool, N)
	used[0] = true
	queue := []Grid{Grid{Idx: 0, Cost: 0}}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for i, q := range T[cur.Idx] {

		}
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
