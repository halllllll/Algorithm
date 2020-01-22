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
	/* --- code ---*/
	// 最大値には届かず、がんばっても二番目にでかいやつとの中間になる
	// 逆に、小さいものと大きいものだと、せっかく大きいものが小さい方に丸められる（ようにみえる）
	// なので、小さいほうから徐々に大きくしていき、どうせ減る差を小さくしていく
	// 初期値は0なので、できるだけ差が小さいやつを採用していくので、結局ソートしたものを採用する
	// ソートしたものを大きい方からK個とったものを小さい方からとっていく。
	n, k := nextInt(), nextInt()
	arr := nextFloats(n)
	sort.Float64s(arr)
	arr = arr[n-k:]
	ans := 0.0
	for _, v := range arr {
		ans = (ans + v) / 2.0
	}
	fmt.Fprint(out, ans)
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
