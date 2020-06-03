package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N := nextInt()
	A := nextInts(N)
	// よくよく考えたら累積和リスト自体が必要なわけではなく結果となった数とその総数だけ欲しいので
	// ruiseki := make([]int, N)
	// ruiseki[0] = A[0]
	r := A[0]
	T := make(map[int]int)
	T[r]++
	for i := 1; i < N; i++ {
		// ruiseki[i] += A[i-1]
		r += A[i]
		T[r]++
	}
	/// T[0]++ // これクソわからんけど多分「2つ選ばなくても総和が0になるとき、ex)1個のときだとncrの計算がうまくいかない」からだと思う
	// 累積和と組み合わせの話してるからてっきり問題文で禁止されているはずの「何も選ばない（部分列が空）」をやってるんじゃねぇかと悩んで1時間くらい無駄にした
	// ↑ってことはncrを無視して最後にT[0]だけを加えてやってもいいということか
	ans := T[0]
	for _, v := range T {
		// if k == 0 { は？これいらんの？と思ったらたしかにそうか 1 -1 1 -1って1と-1と0のぶん2C2あるな
		// 	continue
		// }
		if v > 1 {
			ans += ncr(v, 2)
		}
	}
	fmt.Fprintln(out, ans)
}

func ncr(n, r int) int {
	res := 1
	for i := 1; i <= r; i++ {
		res = res * (n - i + 1) / i
	}
	return res
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}

func nextStrings(n int) []string {
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		ret[i] = next()
	}
	return ret
}

func chars(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
	}
	return ret
}
