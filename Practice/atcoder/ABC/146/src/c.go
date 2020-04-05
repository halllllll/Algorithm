// にぶたんの臭いがする
// 買える最大値の誤読で数十分ほど椅子を温めた
// 何度もWAをして結局写経した
// コード中の①~③が大事っぽい？？？？

package main

import "fmt"

var a, b, x int

func main() {
	fmt.Scan(&a, &b, &x)
	fmt.Println(nibutan(x))
}

func keta(k int) int {
	ret := 0
	for k > 0 {
		ret += 1
		k /= 10
	}
	return ret
}

func nibutan(p int) int {
	l, r := 0, 1000000001 // ① rは上限+1
	// for r-l > 1 {
	for r-l > 1 { // ② 比較は差が1より上
		mid := (l + r) / 2
		f := a*mid + b*keta(mid)
		if p < f {
			// でかすぎる
			r = mid
		} else {
			// まだいける
			l = mid // ③ +1はしない
		}
	}
	return l
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
