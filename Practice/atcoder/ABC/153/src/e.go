// abc153 E
// AOJで無制限ナップザックを倒したあとだったので行けるかと思ったら手こずった（応用する能力が皆無だからね 向いてないね
// WAが取れない ジャッジバグってんじゃねぇのか
// ググったコードの漸化式をパクってみた（解説にこういう細かいケースについての説明はどうせ期待できないので見てない）

package main

import "fmt"

func main() {
	var H, N int
	fmt.Scan(&H, &N)
	As, Bs := make([]int, N), make([]int, N)
	minA, minB := 100000, 100000
	for i := 0; i < N; i++ {
		fmt.Scan(&As[i], &Bs[i])
		if minA > As[i] {
			minA = As[i]
		}
		if minB > Bs[i] {
			minB = Bs[i]
		}
	}
	if H <= minA {
		// どれでも倒せる
		fmt.Println(minB)
		return
	}
	INF := int(1e18)
	DP := make([][]int, N+101) // DP[i][j] := i番目までの魔法を好きなだけ使って数値をj以上にするときの最小の魔力消費値
	for i := 0; i < len(DP); i++ {
		DP[i] = make([]int, H+10101)
		for j := 0; j < H+10101; j++ {
			DP[i][j] = INF
		}
	}
	for i := 0; i < len(DP); i++ {
		DP[i][0] = 0 // 0以下にするのは当然0回でいいので消費魔力も0
	}
	DP[0][0] = 0
	for i := 1; i <= N; i++ {
		for j := 0; j <= H; j++ {
			// if j>=As[i-1]{
			// 	DP[i][j] = min(DP[i-1][j], DP[i][j-As[i-1]]+Bs[i-1])
			// }else{
			// 	DP[i][j] = Bs[i-1]	// 一発で倒せるので
			// }
			// ↓ （解説は見ても意味ないので）ググったらこれが出てきた
			DP[i][j] = min(DP[i-1][j], DP[i][max(0, j-As[i-1])]+Bs[i-1])
			// なんでこれが通って今まで自分が書いたやつが通らないのかは完全に謎
		}
	}
	fmt.Println(DP[N][H])
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
