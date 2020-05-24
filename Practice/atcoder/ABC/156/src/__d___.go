// は？無限に分からんがなんでこれ無限人通してるの？水色だろこれ
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
	N, A, B := nextInt(), nextInt(), nextInt()
	MOD := int(1e9) + 7
	ans := expSqrMod(2, N, MOD) - 1 // 1は何も選ばない場合
	ans -= (combMod(N, A, MOD) + combMod(N, B, MOD))
	if ans < 0 {
		ans += MOD
	}
	fmt.Fprintln(out, ans)
}

func expSqrMod(a, n, mod int) int {
	// 繰り返し二乗法で求めているらしい???????
	ret := 1
	a %= mod
	for n > 0 {
		if n&1 == 1 {
			ret = (ret * a) % mod
		}
		n = n >> 1
		a = (a * a) % mod
	}
	return ret
}
func combMod(n, m, MOD int) int {
	return factorial(n, n-m+1, MOD) * pow(factorial(m, 2, MOD), MOD-2, MOD) % MOD
}

func pow(x, n, MOD int) int {
	r := 1
	for ; n > 0; n /= 2 {
		if n%2 == 1 {
			r = r * x % MOD
		}
		x = x * x % MOD
	}
	return r
}

func factorial(n, m, MOD int) int {
	r := 1
	for i := m; i <= n; i++ {
		r = r * i % MOD
	}
	return r
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
