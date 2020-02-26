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
	// 幅優先での探索は「そのマスにたどり着いたときがそのマスにたどりつく最短手」という特徴がある
	r, c := nextInt(), nextInt()
	sy, sx := nextInt()-1, nextInt()-1
	gy, gx := nextInt()-1, nextInt()-1
	base := make([][]string, r)
	count := make([][]int, r)
	for i := 0; i < r; i++ {
		base[i] = make([]string, c)
		count[i] = make([]int, c)
		line := []rune(next())
		for j := 0; j < c; j++ {
			base[i][j] = string(line[j])
		}
	}
	goal := Pos{x: gx, y: gy}
	queue := []Pos{}
	queue = append(queue, Pos{x: sx, y: sy})
	count[sy][sx] = 1
	steps := []int{0, 1, 0, -1, 0}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if reflect.DeepEqual(goal, cur) { // 構造体のフィールド値での比較はgolangではreflect.DeepEqualを使うらしい
			fmt.Fprintln(out, count[cur.y][cur.x]-1)
			return
		}
		for i := 0; i < 4; i++ {
			next_x, next_y := cur.x+steps[i], cur.y+steps[i+1]
			if next_x < 0 || c <= next_x || next_y < 0 || r <= next_y {
				continue
			}
			if base[next_y][next_x] == "#" || count[next_y][next_x] > 0 {
				continue
			}
			count[next_y][next_x] = count[cur.y][cur.x] + 1
			queue = append(queue, Pos{x: next_x, y: next_y})
		}
	}
}

// -*-*-*-*-*-*-*-*-
// * I/O utilities *
// -*-*-*-*-*-*-*-*-

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
