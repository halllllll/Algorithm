// pythonだとTLEになったのでgoでやる
// 初めてのsortのbinary search
package main

import (
	"bufio"
	"fmt"
	"math"
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
	/* --- code ---*/
	a, b, q := nextInt(), nextInt(), nextInt()
	var INF int
	INF = 1
	for i := 0; i < 18; i++ {
		INF *= 10
	}
	s, t := make([]int, a+2), make([]int, b+2)
	s[0], s[a+1] = -INF, INF
	t[0], t[b+1] = -INF, INF
	for i := 1; i < a+1; i++ {
		s[i] = nextInt()
	}
	for i := 1; i < b+1; i++ {
		t[i] = nextInt()
	}
	for i := 0; i < q; i++ {
		target := nextInt()
		// Searchにわたすの、スライスの長さだけでいいの？スライス自身は必要じゃないの？
		y := float64(sort.Search(len(s), func(j int) bool { return s[j] > target }))
		if y == float64(a+1) {
			y -= 1
		} else if y == 1 {
			y += 1
		}
		x := y - 1
		w := float64(sort.Search(len(t), func(j int) bool { return t[j] > target }))
		if w == float64(b+1) {
			w -= 1
		} else if w == 1 {
			w += 1
		}
		z := w - 1
		result1 := math.Abs(float64(target-s[int(x)])) + math.Abs(float64(s[int(x)]-t[int(w)]))
		result2 := math.Abs(float64(target-s[int(x)])) + math.Abs(float64(s[int(x)]-t[int(z)]))
		result3 := math.Abs(float64(target-s[int(y)])) + math.Abs(float64(s[int(y)]-t[int(w)]))
		result4 := math.Abs(float64(target-s[int(y)])) + math.Abs(float64(s[int(y)]-t[int(z)]))
		result5 := math.Abs(float64(target-t[int(z)])) + math.Abs(float64(t[int(z)]-s[int(x)]))
		result6 := math.Abs(float64(target-t[int(z)])) + math.Abs(float64(t[int(z)]-s[int(y)]))
		result7 := math.Abs(float64(target-t[int(w)])) + math.Abs(float64(t[int(w)]-s[int(x)]))
		result8 := math.Abs(float64(target-t[int(w)])) + math.Abs(float64(t[int(w)]-s[int(y)]))
		var results = []float64{result1, result2, result3, result4, result5, result6, result7, result8}
		sort.Float64s(results)
		result0 := int(results[0])
		fmt.Fprintln(out, result0)

	}
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
