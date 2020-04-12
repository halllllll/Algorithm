// きりみんちゃんの配信からきました
// 左右をとる+-1のしゃくとり、左がマイナスかつ右がプラスの場合には「左に行った後折り返す」vs「右に行ったあと折り返す」が発生する
// 0を含む場合の取扱いに注意
package main

import (
	"fmt"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	a := make([]int, n)
	includeZero := false
	zeroIdx := -1
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		a[i] = j
		if j == 0 {
			includeZero = true
			zeroIdx = i
		}
	}
	if includeZero {
		// ゼロを含む場合、よくわかんなかったので近い値で更新することにした
		if zeroIdx != 0 && zeroIdx != n-1 {
			if abs(a[zeroIdx-1]) < abs(a[zeroIdx+1]) {
				a[zeroIdx] = a[zeroIdx-1]
			} else {
				a[zeroIdx] = a[zeroIdx+1]
			}
		}
	}
	ans := 10000000000000000
	r := 0
	tmp := 0
	// しゃくとりフェーズ
	for l := 0; l <= n-k; l++ {
		for r < n && r-l < k {
			r += 1
		}
		// 更新は3パターン
		if a[r-1] <= 0 {
			// 最大で0より小さい場合
			tmp = a[l] * -1
		} else if a[l] >= 0 {
			// 最小で0より大きい場合
			tmp = a[r-1]
		} else {
			// 最小が0より小さく、最大が0より大きい場合
			tmp = min(a[l]*-2+a[r-1], a[r-1]*2+a[l]*-1)
		}
		ans = min(ans, tmp)
	}
	fmt.Println(ans)
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a < 0 {
		a *= -1
	}
	return a
}
