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
	// 令和C最大級に日本語がむずかしい かといって英語もむずかしい
	// スイッチの状態をbit全探索する
	n, m := nextInt(), nextInt()
	balbs := make([][]int, m)
	for i := 0; i < m; i++ {
		k := nextInt()
		balbs[i] = make([]int, k)
		for j := 0; j < k; j++ {
			balbs[i][j] = nextInt() - 1
		}
	}
	ans := 0
	ps := nextInts(m)
	// スイッチがn個あるのでそれのオンオフの状態 2^nぶん
	// ループでやるの毎回わけわからんな
	for i := 0; i < (1 << n); i++ {
		ok := true
		for j := 0; j < m; j++ {
			c := 0
			for _, b := range balbs[j] {
				if (i>>b)&1 == 1 {
					c += 1
				}
			}
			c %= 2
			if c != ps[j] {
				ok = false
			}
		}
		if ok {
			ans += 1
		}
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
