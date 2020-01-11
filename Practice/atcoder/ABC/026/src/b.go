package main

import (
	"bufio"
	"fmt"
	"os"
	// "reflect"
	"strconv"
	"math"
	"sort"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	n := nextInt()
	input := make([]float64)
	for i:=0; i<n; i++{
		append(input, nextFloat64())
	}
	sort.Ints(input)
	ans := 0
	fmt.Println(input)
	fmt.Printf(out, ans)
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