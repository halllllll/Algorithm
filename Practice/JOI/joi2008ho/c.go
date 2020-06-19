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

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code --- */
	// ちっともわからんので解説をググった
	// 半分全列挙してにぶたんらしい

	n, m := nextInt(), nextInt()
	points := make([]int, n+1)
	points[0] = 0
	for i := 1; i <= n; i++ {
		points[i] = nextInt()
	}

	// 半分列挙 1+2+3+..+n+(n+1)個
	arr := make([]int, factorialOf(n+1))
	c := 0
	for i := 0; i <= n; i++ {
		for j := i; j <= n; j++ {
			arr[c] = points[i] + points[j]
			c += 1
		}
	}
	sort.Ints(arr) // これで4本のバレルのうち2本ぶんの得点の全列挙が完了 この中からにぶたんで探す

	// 残り2本を全探索して足して、mから引いたものをtargetにしてにぶたんで探して更新

	ans := 0
	for i := 0; i < n+1; i++ {
		for j := i; j < n+1; j++ {
			p := f(arr, m-(points[i]+points[j]))
			if m < p {
				continue
			}
			if points[i]+points[j]+p <= m {
				ans = max(ans, points[i]+points[j]+p)
			}
		}
	}
	fmt.Fprintln(out, ans)
}

func f(arr []int, target int) int {
	// ほしいのは targetを超えない最大の値
	l, r := 0, len(arr)
	for r-l > 1 {
		mid := (l + r) / 2
		if arr[mid] < target {
			l = mid
		} else {
			r = mid
		}
	}
	return arr[l]
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
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

// -*-*-*-*-*-
// * nibutan *
// -*-*-*-*-*-
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

// *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
// * math flavor typical theories *
// *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
func gcd(a, b int) int {
	if a > b {
		return gcd(b, a)
	}
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

func pow(a, b int) (ret int) {
	ret = a
	// 10^2 = 100ってことは10に10を1回掛けることだね
	// なので初期値を含めると上限b-1未満
	for i := 0; i < b-1; i++ {
		ret *= a
	}
	return
}

func powMod(n, m, mod int) (ret int) {
	ret = 1
	for m > 0 {
		if m&1 == 1 {
			ret *= n
			ret %= mod
		}
		n *= n
		n %= mod
		m >>= 1
	}
	return ret
}

func factorialOf(n int) (ret int) {
	ret = 0
	for i := 0; i <= n; i++ {
		ret += i
	}
	return
}
