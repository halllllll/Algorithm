package main

// python3がTLEなるのでGoでやってみる
// GoでもTLEなった... 再帰じゃなくてループでやるか
// とおもったけどやりかたがまっっっったくわからんくて保留

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"reflect"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)
var d int
var s string

var dp [][][]int
var length int

// var dp [10001][2][101]int
var MOD int

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	d = nextInt()
	s = next()
	length = len([]rune(s))
	MOD = int(math.Pow(10, 9)) + 7
	//  +1はテキトー
	dp = make([][][]int, length+1)
	// 初期化 とりあえず-1で埋める
	for i := 0; i < length+1; i++ {
		dp[i] = make([][]int, 2)
		for j := 0; j < 2; j++ {
			dp[i][j] = make([]int, d+1)
			for k := 0; k <= d; k++ {
				dp[i][j][k] = -1
			}
		}
	}
	// 流儀じゃないがしかたないのでループでDPやる
	dp[0][0][0] = 1
	for i := 0; i < length; i++ {
		for j := 0; j < 2; j++ {
			var upper int
			var next_smaller int
			if j == 0 {
				_upper, _ := strconv.ParseInt(string([]rune(s)[i]), 10, 64)
				upper = int(_upper)
			} else {
				upper = 9
			}
			for k := 0; k <= upper; k++ {
				v, _ := strconv.ParseInt(string([]rune(s)[i]), 10, 64)
				if j == 1 || k < int(v) {
					next_smaller = 1
				} else {
					next_smaller = 0
				}
				if k == upper{
					dp[i+1][0][()]
				}

			}
		}
	}
	ans := rec(0, 0, 0) - 1 // 0を含んでいるので
	fmt.Fprint(out, ans)
}

func rec(i, smaller, cur int) int {

	if i == length {
		if cur == 0 {
			dp[i][smaller][cur] = 1
		} else {
			dp[i][smaller][cur] = 0
		}
		return dp[i][smaller][cur]
	}
	if dp[i][smaller][cur] >= 0 {
		return dp[i][smaller][cur]
	}

	ret := 0
	var upper int
	if smaller == 1 {
		upper = 9
	} else {
		_upper, _ := strconv.ParseInt(string([]rune(s)[i]), 10, 64)
		upper = int(_upper)
	}

	for j := 0; j <= upper; j++ {
		var next_smaller int
		v, _ := strconv.ParseInt(string([]rune(s)[i]), 10, 64)
		if smaller == 1 || j < int(v) {
			next_smaller = 1
		} else {
			next_smaller = 0
		}
		ret += rec(
			i+1,
			next_smaller,
			(cur+j)%d,
		)
	}
	ret %= MOD
	dp[i][smaller][cur] = ret
	return ret
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
