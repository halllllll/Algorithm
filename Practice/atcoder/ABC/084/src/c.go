// ぱっと見むずいがにぶたんの臭いがする
// 一瞬誤読して実際に作ったやつ省くんかと思ったが種類だけを聞いているんだった
// TLEになりやがったのでbufioを使う
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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
	A, B, C := nextInts(N), nextInts(N), nextInts(N)
	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	sort.Ints(B)
	sort.Ints(C)
	ans := 0
	for i := 0; i < N; i++ {
		// ascendingのときreverseしなきゃいけないのか....
		left := sort.Search(N, func(j int) bool {
			return A[j] < B[i]
		})
		right := sort.Search(N, func(j int) bool {
			return C[j] > B[i]
		})
		if left == N || right == N {
			// golangのバイナリサーチで見つからないとき下でも上でもこれになるらしい
			continue
		}
		ans += (N - left) * (N - right)
	}
	fmt.Fprintln(out, ans)
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
