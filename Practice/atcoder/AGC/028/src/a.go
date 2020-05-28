// lはlcmでよさそう（勘
// あとは順に埋めていって矛盾があれば終了 余ったところは適当に"a"入れればいいけど長さを答える問題なので必要ないね
// 意味不明だがTLEになる
// は？辞書かよ... 後出しだけど10^5どうしのLCMそのまんま使ってX作ろうとしてたのが駄目

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
	defer out.Flush() // !!!!caution!!!! you must use Fprint(out, ) not Print()
	N, M := nextInt(), nextInt()
	SS, TT := chars(next()), chars(next())
	L := lcm(N, M)
	// X := make([]string, L)
	X := make(map[int]string)
	for i := 0; i < N; i++ {
		idx := i * L / N
		X[idx] = SS[i]
	}
	flag := true
	for i := 0; i < M; i++ {
		idx := i * L / M
		if _, ok := X[idx]; ok {
			if X[idx] == TT[i] {
				continue
			} else {
				flag = false
				break
			}
		}
	}
	if flag {
		fmt.Fprintln(out, L)
	} else {
		fmt.Fprintln(out, -1)
	}
}

func lcm(a, b int) int {
	return (a * b) / gcd(a, b)
}

func gcd(a, b int) int {
	if a > b {
		a, b = b, a
	}
	for a > 0 {
		a, b = b%a, a
	}
	return b
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func chars(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
	}
	return ret
}
