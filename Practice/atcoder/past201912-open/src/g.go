// 全探索のこころ
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var N int
	fmt.Scan(&N)
	T := make([][]int, N)
	for i := 0; i < N; i++ {
		T[i] = make([]int, N)
	}
	// まずもってこのテーブル作るの頭使うよね
	for i := 0; i < N; i++ {
		for j := 0; j < N-i-1; j++ {
			var V int
			fmt.Scan(&V)
			T[i][i+j+1], T[i+j+1][i] = V, V
		}
	}
	ans := -pow(10, 10)
	// pow(3, N), なるほどという感じ（N個それぞれ012のどれか）
	for bit := 0; bit < pow(3, N); bit++ {
		t := chars(padLeft(baseConvert(bit, 3), "0", N))
		tmp := 0
		for i := 0; i < N; i++ {
			for j := i + 1; j < N; j++ {
				if i != j && t[i] == t[j] {
					tmp += T[i][j]
				}
			}
		}
		ans = max(ans, tmp)
	}
	fmt.Println(ans)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func chars(s string) (ret []string) {
	ret = make([]string, len(s))
	for i, c := range []rune(s) {
		ret[i] = string(c)
	}
	return
}

func padLeft(s string, pad string, plength int) string {
	for i := len(s); i < plength; i++ {
		s = pad + s
	}
	return s
}

func baseConvert(n, x int) string {
	// nのx進数表記したstringを返す
	if n == 0 {
		return ""
	}
	ret := strconv.Itoa(n % x)
	ret = baseConvert(n/x, x) + ret
	return ret
}

func pow(a, x int) int {
	if x == 0 {
		return 1
	}
	ret := 1
	for x > 0 {
		ret *= a
		x--
	}
	return ret
}
