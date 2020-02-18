package main

// 某DP, 再帰でやったらTLEになる原因がメモ化再帰しか浮かばないんだけどループでやるDPってやったことないので練習のため来ました
// もう初心にかえってナップザックをやる

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"reflect"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)
var n, w int
var values, weights []int
var dp [101][10101]int // C++でよくみる初期化

func rec(i, cur_w int) int {
	if dp[i][cur_w] > 0 {
		return dp[i][cur_w]
	}
	res := 0
	if i >= n {
		res = 0
	} else if cur_w < weights[i] {
		// このi番目の商品はキャパオーバーするので選択することができない
		res = rec(i+1, cur_w)
	} else {
		// この商品は選択することができるので、選択しなかった場合と選択した場合を試して価値が大きい方を採用する
		res = int(math.Max(float64(rec(i+1, cur_w)), float64(rec(i+1, cur_w-weights[i])+values[i])))
	}
	dp[i][cur_w] = res
	return dp[i][cur_w]
}

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	n, w = nextInt(), nextInt()
	values, weights = make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		vi, wi := nextInt(), nextInt()
		values[i] = vi
		weights[i] = wi
	}
	fmt.Fprint(out, rec(0, w))
	fmt.Fprint(out, "\n")
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func nextFloat64() float64 {
	a, _ := strconv.ParseFloat(next(), 64)
	return a
}

func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}
func nextFloats(n int) []float64 {
	ret := make([]float64, n)
	for i := 0; i < n; i++ {
		ret[i] = nextFloat64()
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

func PrintOut(src interface{}, joinner string) {
	switch reflect.TypeOf(src).Kind() {
	case reflect.Slice:
		s := reflect.ValueOf(src)
		for idx := 0; idx < s.Len(); idx++ {
			fmt.Fprintf(out, "%v", s.Index(idx))
			if idx < s.Len()-1 {
				fmt.Fprintf(out, "%s", joinner)
			} else {
				fmt.Fprintln(out)
			}
		}
	default:
		fmt.Fprintln(out, "fuck")
	}
}
