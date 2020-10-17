// 後ろのほうで選択肢を多くするためには少ない方からとっていくほうがいい
// なんかうまくいかんかったので後ろやら大きい順にやっていくことにする
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Data struct {
	N int
	K string
}

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N := nextInt()
	A, B := nextInts(2*N), nextInts(2*N)
	now := int(1e18)
	ai, bi := 0, 0
	ans := make([]string, 2*N)
	for i := 2*N - 1; i >= 0; i-- {
		if now >= A[i] && now >= B[i] && ai < N && bi < N {
			if A[i]-now >= B[i]-now {
				now = A[i]
				ans[i] = "A"
				ai++
			} else {
				now = B[i]
				ans[i] = "B"
				bi++
			}
		} else if now >= A[i] && ai < N {
			now = A[i]
			ans[i] = "A"
			ai++
		} else if now >= B[i] && bi < N {
			now = B[i]
			ans[i] = "B"
			bi++
		} else {
			fmt.Fprintln(out, -1)
			return
		}
	}
	fmt.Fprintln(out, strings.Join(ans, ""))
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
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
