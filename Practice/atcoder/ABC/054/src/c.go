package main

// かなり雑にdfs書いた

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

var table [][]bool

func dfs(passed []bool, cur, limit int) int {
	count := 0
	for _, v := range passed {
		if v == true {
			count += 1
		}
	}
	if count == limit {
		return 1
	}
	ret := 0
	for i, v := range table[cur] {
		if v && !passed[i] {
			my_passed := append([]bool{}, passed...)
			my_passed[i] = true
			ret += dfs(my_passed, i, limit)
		}
	}
	return ret
}

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	n, m := nextInt(), nextInt()
	// table初期化
	table = make([][]bool, n)
	for i := 0; i < n; i++ {
		table[i] = make([]bool, n)
	}

	for i := 0; i < m; i++ {
		a, b := nextInt()-1, nextInt()-1
		table[a][b] = true
		table[b][a] = true
	}
	passed := make([]bool, n)
	passed[0] = true
	fmt.Fprint(out, dfs(passed, 0, n))
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
