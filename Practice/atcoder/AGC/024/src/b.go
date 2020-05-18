// 理屈はしらんけどサンプル眺めてたら差1で最長増加部分列ぶん以外並び替える感じになりました
// （後出しだけど途中に挿入できないからでしょう。）
// 探索が分からんけどインデックスを保持するmapで探索していけないだろうか
// （計算量はいつもながら不明です）
// ようわからんけどLCS忘れたからしゃくとりっぽいのでやった

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	P := make([]int, N)
	T := make(map[int]int)
	Q := make([]int, N+1)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		P[i] = V
		T[V] = i + 1
		Q[V] = i + 1
	}
	fmt.Println(Q)
	lnh := 0
	r := 0
	for l := 1; l <= N; {
		tmp := T[l]
		for r = l + 1; r <= N && tmp < T[r]; {
			tmp = T[r]
			r++
		}
		lnh = max(lnh, r-l)
		l = r
	}
	fmt.Println(N - lnh)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
