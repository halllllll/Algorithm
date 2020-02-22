package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

var n int
var h, s []int

func check(target int) bool {
	upper_limit_of_breaking_baloon := make([]int, n)
	for i := 0; i < n; i++ {
		x := (target - h[i]) / s[i]
		if target < h[i] {
			return false
		}
		upper_limit_of_breaking_baloon[i] = x
	}
	sort.Ints(upper_limit_of_breaking_baloon)
	// 割って試す
	for i := 0; i < n; i++ {
		if upper_limit_of_breaking_baloon[i] < i {
			return false
		}
	}
	return true
}

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code --- */
	// にぶたんで決め打ちまではわかったが、そのあと「早く割らねばならないやつから貪欲で割って試す」が浮かばず....
	// これも解答みて書いてみてなんかしらんけどどーーーーーーしても通らなかったので適当にggって出たやつを写経しただけで、つまりは一切理解をしていないということだ あたまがわるいからだね

	n = nextInt()
	h = make([]int, n)
	s = make([]int, n)
	for i := 0; i < n; i++ {
		h[i], s[i] = nextInt(), nextInt()
	}
	l, r := 0, 100000000000000000
	// for l < r { これじゃなくて
	for r-l > 1 { // これ
		mid := (l + r) / 2
		if check(mid) {
			// l = mid + 1 これじゃなくて
			r = mid // これ
		} else {
			//r = mid	これじゃなくて
			l = mid // これ
		}
	}
	// fmt.Fprintln(out, l)	 これじゃなくて
	fmt.Fprintln(out, r) // これ
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

func split(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
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

// nibutan
func lower_bound(arr []int, target int) int {
	l, r := 0, len(arr)
	for l < r {
		mid := (l + r) / 2
		if arr[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	return l
}

func upper_bound(arr []int, target int) int {
	l, r := 0, len(arr)
	for l < r {
		mid := (l + r) / 2
		if target < arr[mid] {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}
