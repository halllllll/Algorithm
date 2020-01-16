package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	a, b, c := strings.ToUpper(next()), strings.ToUpper(next()), strings.ToUpper(next())
	as, bs, cs := len(a), len(b), len(c)
	ai, bi, ci := 0, 0, 0
	cur := "A"
	for ;; {
		if cur == "A"{
			if ai == as{
				fmt.Fprint(out, cur)
				return
			}else{
				cur = string(a[ai])
				ai ++
			}
		}else if cur == "B"{
			if bi == bs{
				fmt.Fprint(out, cur)
				return
			}else{
				cur = string(b[bi])
				bi ++
			}
		}else if cur == "C"{
			if ci == cs{
				fmt.Fprint(out, cur)
				return
			}else{
				cur = string(c[ci])
				ci ++
			}
		}
	}
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int64 {
	a, _ := strconv.Atoi(next())
	return int64(a)
}

func nextFloat64() float64 {
	a, _ := strconv.ParseFloat(next(), 64)
	return a
}

func nextInts(n int) []int64 {
	ret := make([]int64, n)
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
