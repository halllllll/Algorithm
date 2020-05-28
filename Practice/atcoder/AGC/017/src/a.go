// P=0だと奇数は偶数個選ぶ nCrを持ってくる
package main

import "fmt"

func main() {
	var N, P int
	fmt.Scan(&N, &P)
	evens, odds := 0, 0
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if V%2 == 0 {
			evens++
		} else {
			odds++
		}
	}
	ea := 0
	oa := 0
	if P == 0 {
		// 偶数をいくつでも、奇数は偶数個、0を含む
		for i := 0; i <= evens; i++ {
			ea += ncr(evens, i)
		}
		for i := 0; i <= odds; i += 2 {
			oa += ncr(odds, i)
		}
	} else {
		// 偶数をいくつでも、奇数は奇数個
		for i := 0; i <= evens; i++ {
			ea += ncr(evens, i)
		}
		for i := 1; i < odds; i += 2 {
			oa += ncr(odds, i)
		}
	}
	fmt.Println(ea * oa)
}

func ncr(n, r int) int {
	res := 1
	for i := 1; i <= r; i++ {
		res = res * (n - i + 1) / i
	}
	return res
}
