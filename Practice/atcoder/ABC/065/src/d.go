package main

import (
	"fmt"
	"sort"
)

var n int
var edges_origin []Edge
var edges []Edge

type Edge struct {
	x, y, idx, cost int
}

// atcoderのgolangがいつまでたっても古いせいでたかだか構造体のソートにこんな実装を書かなきゃならない羽目になる
type ByX []Edge
type ByY []Edge
type ByCost []Edge

func (_e ByX) Len() int           { return len(_e) }
func (_e ByX) Swap(i, j int)      { _e[i], _e[j] = _e[j], _e[i] }
func (_e ByX) Less(i, j int) bool { return _e[i].x < _e[j].x }

func (_e ByY) Len() int           { return len(_e) }
func (_e ByY) Swap(i, j int)      { _e[i], _e[j] = _e[j], _e[i] }
func (_e ByY) Less(i, j int) bool { return _e[i].y < _e[j].y }

func (_e ByCost) Len() int           { return len(_e) }
func (_e ByCost) Swap(i, j int)      { _e[i], _e[j] = _e[j], _e[i] }
func (_e ByCost) Less(i, j int) bool { return _e[i].cost < _e[j].cost }

func main() {
	// MSTに落とし込みたいがNが大きすぎる
	// 二次元座標のグラフはどちらかの軸でソートしてみるとみえてくるものがある
	// xでソートしたとき、明らかにその順番にノードを選ぶとよさそう（x1->x2->x3とx1->x3->x2を比べると後者はいったん行き過ぎてから戻るため無駄がある）
	// ではyも考えるとするとどうなるか？で詰んだ。

	// 「x,yそれぞれでソートしてみると、『2点間を貼るエッジが2つ存在する』となる」
	// なのでエッジ数は2(N-1)となりMSTができそうになる
	// （そこからMSTをやるのがまたなんかめんどくさかったんだけどそれは別の話）

	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var x, y int
		fmt.Scan(&x, &y)
		e := Edge{x: x, y: y, idx: i}
		edges_origin = append(edges_origin, e)
	}
	sort.Sort(ByX(edges_origin))
	for i := 1; i < n; i++ {
		payload := abs(edges_origin[i-1].x - edges_origin[i].x)
		edges = append(edges, Edge{x: edges_origin[i-1].idx, y: edges_origin[i].idx, cost: payload})
	}
	sort.Sort(ByY(edges_origin))
	for i := 1; i < n; i++ {
		payload := abs(edges_origin[i-1].y - edges_origin[i].y)
		edges = append(edges, Edge{x: edges_origin[i-1].idx, y: edges_origin[i].idx, cost: payload})
	}
	sort.Sort(ByCost(edges))
	ans := 0
	parents := make([]int, n)
	for i := 0; i < n; i++ {
		parents[i] = i
	}
	for _, e := range edges {
		if same(e.x, e.y, parents) == false {
			union(e.x, e.y, parents)
			ans += e.cost
		}
	}
	fmt.Println(ans)
}

func root(x int, arr []int) int {
	if x == arr[x] {
		return x
	}
	y := root(arr[x], arr)
	arr[x] = y
	return arr[x]
}

func same(a, b int, arr []int) bool {
	return root(a, arr) == root(b, arr)
}

func union(a, b int, arr []int) {
	ra, rb := root(a, arr), root(b, arr)
	arr[ra] = rb
}

func abs(a int) int {
	if a <= 0 {
		return -1 * a
	} else {
		return a
	}
}
