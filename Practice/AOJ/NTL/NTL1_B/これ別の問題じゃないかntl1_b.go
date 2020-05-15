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
	/* --- code --- */
	// 負の閉路にも対応できるワ―シャルフロイドを使う
	v, e := nextInt(), nextInt()
	INF := pow(10, 16)
	table := make([][]int, v)
	for i:=0; i<v; i++{
		table[i] = make([]int, v)
		for j:=0; j<v; j++{
			if i!=j{
				table[i][j] = INF
			}else{
				table[i][j] = 0
			}
		}
	}
	for i:=0; i<e; i++{
		s,t,d := nextInt(), nextInt(), nextInt()
		table[s][t] = d
		// table[t][s] = d
	}
	for k:=0; k<v; k++{
		for i:=0; i<v; i++{
			// この判定が必要
			if table[i][k] == INF{
				continue
			}
			for j:=0; j<v; j++{
				// この判定が必要
				if table[k][j] == INF{
					continue
				}
				table[i][j] = min(table[i][j], table[i][k]+table[k][j])
			}
		}
	}
	for i, t := range table{
		for j, tv := range t{
			if table[j][j] < 0 || table[i][i] < 0{
				fmt.Println("NEGATIVE CYCLE")
				os.Exit(0) // returnだとなんか処理が生きてて駄目だった
			}
			if tv == INF{
				fmt.Fprint(out, "INF")
			}else{
				fmt.Fprint(out, tv)
			}
			if j < v-1{
				fmt.Fprint(out, " ")
			}
		}
		fmt.Fprintln(out)
	}
}

func min(a, b int)int{
	if a < b{
		return a
	}
	return b
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

func pow(a, b int) (ret int) {
	ret = a
	// 10^2 = 100ってことは10を2回掛けることだね
	// なので上限b-1未満
	for i := 0; i < b-1; i++ {
		ret *= a
	}
	return
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
