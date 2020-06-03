package main

// 某DP, 再帰でやったらTLEになる原因がメモ化再帰しか浮かばないんだけどループでやるDPってやったことないので練習のため来ました

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

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	n := nextInt()
	h := nextInts(n)
	ans := make([]int, n)
	INF := int(math.Pow(10, 9))
	for i := 0; i < n; i++ {
		ans[i] = INF
	}
	ans[0] = 0
	for i := 1; i < n; i++ {
		if i == 1 {
			// 最初の1手しか進めない
			ans[i] = int(math.Min(float64(ans[i]), float64(ans[i-1]+int(math.Abs(float64(h[i]-h[i-1]))))))
		} else {
			// ひとつまえかふたつまえの小さい方
			pre_one := float64(ans[i-1]) + math.Abs(float64(h[i]-h[i-1]))
			pre_two := float64(ans[i-2]) + math.Abs(float64(h[i]-h[i-2]))
			ans[i] = int(math.Min(pre_one, pre_two))
		}
	}
	fmt.Fprint(out, ans[n-1])
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
