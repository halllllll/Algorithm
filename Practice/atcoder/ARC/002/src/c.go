// かぶらないようにしたいので2回探索する
// 脳死で12パターン全部でいいのか？ -> 重複していいので16パターンだった
package main

import (
	"fmt"
	"strings"
)

func main() {
	var N int
	fmt.Scan(&N)
	var S string
	fmt.Scan(&S)
	T := make([]string, N)
	for i, c := range []rune(S) {
		T[i] = string(c)
	}
	pattern := []string{"AA", "BB", "XX", "YY", "AB", "BA", "AX", "XA", "AY", "YA", "BX", "XB", "BY", "YB", "XY", "YX"}
	ans := int(1e10)
	for _, p := range pattern {
		firstCount := strings.Count(S, p)
		// fmt.Printf("最初のパターン: %s で区切った場合のカウント %d\n", p, firstCount)
		TT := strings.Split(S, p)
		// fmt.Printf("		target: %v\n", TT)
		for _, pp := range pattern {
			if p == pp {
				continue
			}
			secondCount := 0
			for _, tt := range TT {
				secondCount += strings.Count(tt, pp)
			}
			rest := N - 2*firstCount - 2*secondCount
			ans = min(ans, rest+firstCount+secondCount)
			// fmt.Printf("		2回目のパターン %s で区切った場合のカウント %d \n", pp, secondCount)
			// fmt.Printf("		rest = N-2*(1回目+2回目) = %d\n", rest)
		}
	}
	fmt.Println(ans)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
