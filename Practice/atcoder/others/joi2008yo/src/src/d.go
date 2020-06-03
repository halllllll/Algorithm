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

type Pos struct {
	x, y int
}

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code --- */
	// 星座に含まれる一個だけを基準として、以降探索していく。
	// 星図のもののうちひとつを選んだ1つの星座の座標と比較して、その差を基準として、それぞれ別の座標を比較していく。n個一致すればおｋ
	// うーん 実装しにくい。。。

	n := nextInt()
	constellation := make([]Pos, n) // コンステレーション、星座、っていうらしいよ
	for i := 0; i < n; i++ {
		x, y := nextInt(), nextInt()
		p := &Pos{x, y}
		constellation[i] = *p
	}
	m := nextInt()
	astronomical_map := make([]Pos, m) // これは星図だね
	for i := 0; i < m; i++ {
		x, y := nextInt(), nextInt()
		p := &Pos{x, y}
		astronomical_map[i] = *p
	}

	pick := constellation[0]
	for _, p := range astronomical_map{
		assume_dif := &Pos{pick.x - p.x, pick.y - p.y}
		count := 0
		for i:=1; i<n; i++{
			cur_star := constellation[i]
			cur_star_dif = &Pos{cur_star.x - }
		}
	}
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
