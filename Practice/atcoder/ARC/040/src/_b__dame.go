// 右側で直近にある.から2*Rぶんを1ターンで倒せると思えば区間スケジューリングぽい気がするが実装がよくわからん
// ちゃうわ 初手から...の場合があるので自分より後ろは考えなくていいのでは
// いうて理不尽なくらいNが小さいんだが..
// DPか？ とりあえず脳死メモ再帰
package main

import (
	"fmt"
	"strings"
)

var N, R int
var S []string
var DP [][]int
var INF int

func main() {
	fmt.Scan(&N, &R)
	S = make([]string, N)
	DP = make([][]int, 110)
	INF = int(1e10)
	for i := 0; i < 110; i++ {
		DP[i] = make([]int, 110)
		for j := 0; j < 110; j++ {
			DP[i][j] = INF
		}
	}
	var T string
	fmt.Scan(&T)
	rest := 0
	for i, c := range []rune(T) {
		S[i] = string(c)
		if string(c) == "." {
			rest++
		}
	}
	if R == 1 {
		// 自分がいるマスしか塗れないので
		fmt.Println(strings.LastIndex(T, ".") + rest)
		return
	}
	fmt.Println(rec(S, 0, rest))
}

func rec(L []string, i, r int) int {
	fmt.Printf("no l : %v\n", L)
	if DP[i][r] < INF {
		return DP[i][r]
	}
	if r == 0 {
		fmt.Println("殲滅完了")
		return 0
	}
	if i == N || N-i < r {
		// 最後まできてしまった or 残りを倒せない
		fmt.Printf("見逃し")
		return INF
	}
	ret := 0
	hit := 0
	nexL := append([]string{}, L...)
	for j := i; j < min(i+R, N); j++ {
		if L[j] == "." {
			hit++
		}
		nexL[j] = "o"
	}
	if hit == 0 {
		// うたねぇほうがいいにきまってる
		ret += rec(L, i+1, r) + 1
	} else {
		// 進むか打つか選べる
		ret += min(rec(nexL, i, r-hit), rec(L, i+1, r)) + 1
	}
	DP[i][r] = ret
	return ret
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
