package main

// ぜんぜんわからん
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
	// bit全探索使うってのを気づきにくい問題（文）じゃないかこれ union find使いたくなったら負け
	n, m := nextInt(), nextInt()
	// どうせx<yなので雑にやってもいいけど隣接行列にするのであんま意味なかった
	table := make([][]bool, n)
	for i := 0; i < n; i++ {
		table[i] = make([]bool, n)
	}
	for i := 0; i < m; i++ {
		// 一人しかいない場合もあるってんで、自分自身も自分の友達ということにするわ
		table[i][i] = true
		x, y := nextInt()-1, nextInt()-1
		table[x][y] = true
		table[y][x] = true
	}

	ans := 0
	// n人のうち陣営に取り込むやつの組み合わせをbit全探索
	for i := 0; i < (1 << uint64(n)); i++ {
		tmp := 0
		include := make([]bool, n)
		for j := 0; j < n; j++ {
			// そもそもjは取り込めるか？
			if 1&(i>>uint64(j)) == 0 {
				// fmt.Printf("i=%vにおいて j=%vはビットが立ってないので取り込めない\n", i, j)
				continue
			}
			include[j] = true
			// jのともだちを取り込むとき、jのおともだちのビットも立っていなければならない
			for k, v := range table[j] {
				if v == true && include[k] == false {
					include[k] = true
					tmp += 1
				}
			}
		}

		ans = max(ans, tmp)
	}
	fmt.Fprintln(out, ans)
}

func max(a, b int) int {
	if a < b {
		return b
	} else {
		return a
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
