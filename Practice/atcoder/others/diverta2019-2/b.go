// ベクトル同じならコストかからない とするとベクトルっつーか同一直線上にあるものは同じ木に属するとして木の数を数える感じ（まずこの読解で天才みを感じる
// つっても実装がまったく浮かばない ベクトルはキメれるとして探索は？
// 1つの点に対して決め打ちしたベクトルで到達できるのはたかだか1つなのでそれがあったら0なければ1って感じか？？

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	X, Y := make([]int, N), make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&X[i], &Y[i])
	}
	ans := int(1e18)
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			vectorX, vectorY := X[i]-X[j], Y[i]-Y[j]
			// 今キメたベクトルでいくつ対応できるか
			tmp := 0
			for y := 0; y < N; y++ {
				flag := false
				for x := 0; x < N; x++ {
					if y == x {
						continue
					}
					if X[y]-X[x] == vectorX && Y[y]-Y[x] == vectorY {
						flag = true
						break
					}
				}
				// 対応できるのがなかったね これはコスト必須
				if !flag {
					tmp++
				}
			}
			ans = min(ans, tmp)
		}
	}
	fmt.Println(ans)
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
