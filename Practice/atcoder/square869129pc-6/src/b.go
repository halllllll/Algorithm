package main

import (
	"bufio"
	"fmt"
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
	// 愚なパターンは、aの最小値より小さい値を入り口に、bの最大値より大きい値を出口にする場合。
	// -> Aのうちどれかを入り口に、Bのうちどれかを出口にすればよさそう。という全探索
	n := nextInt()
	a, b := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		a[i], b[i] = nextInt(), nextInt()
	}
	ans := 1000000000000
	for _, start := range a {
		for _, goal := range b {
			dif := 0
			for i := 0; i < n; i++ {
				dif += abs(start - a[i])
				dif += abs(a[i] - b[i])
				dif += abs(b[i] - goal)
			}
			ans = min(ans, dif)
		}
	}
	fmt.Fprintln(out, ans)
}

func abs(x int) int {
	if x < 0 {
		return x * -1
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
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
