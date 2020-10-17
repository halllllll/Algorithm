package main

import (
	"fmt"
)

var n, q int

type SegmentTree struct {
	n, k       int
	base, tree []int
}

func (st *SegmentTree) init() {
	if st.n < 1 {
		return
	}
	sz := st.n

	// 配列baseをセグ木で表現する。2^k-1個の配列をセグ木として使う
	st.k = 1
	for st.k < sz {
		st.k *= 2
	}
	st.tree = make([]int, 2*st.k-1)
	// // 葉から初期化する 最下層はk-1個なので+k-1でアクセス可能
	// for i := 0; i < sz; i++ {
	// 	st.tree[i+k-1] = st.base[i]
	// }
	// // 葉から根にむかって更新
	// for i := n - 2; i >= 0; i-- {
	// 	st.tree[i] = min(st.tree[2*i+1], st.tree[2*i+2])
	// }

	// ... この問題だとbaseがなくて最初からすべて1<<31-1で埋めた感じになるのでアドホックに
	for i := 0; i < 2*st.k-1; i++ {
		st.tree[i] = 1<<31 - 1
	}
}

func (st *SegmentTree) update(i, x int) {
	// 更新処理は葉からさかのぼっていく
	// whileでやるのでここで最下段のノードにアクセスする
	i += st.k - 1
	st.tree[i] = x
	for i > 0 {
		i = (i - 1) / 2 // ひとつ上の段に移動
		st.tree[i] = min(st.tree[2*i+1], st.tree[2*i+2])
	}
}
func (st *SegmentTree) find(i, x int) int {
	// findは根からくだっていく
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	fmt.Scan(&n)
	fmt.Scan(&q)
	st := SegmentTree{n: n}
	st.init()
	for i := 0; i < q; i++ {
		var query, p, q int
		fmt.Scan(&query)
		fmt.Scan(&p)
		fmt.Scan(&q)
		if query == 0 {

		} else {

		}
	}
}
