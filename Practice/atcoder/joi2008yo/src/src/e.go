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
	// rをbit全探索したあと、縦の串のr個のうち1が半分より多いところをひっくり返すようにする
	r, c := nextInt(), nextInt()
	table := make([][]int, r)
	for i := 0; i < r; i++ {
		table[i] = nextInts(c)
	}
	ans := 0
	for i := 0; i < (1 << uint64(r)); i++ {
		// tmp := 0
		new_table := append([][]int{}, table...)
		for j := 0; j < r; j++ {
			if 1&(i>>uint64(j)) == 1 {
				// 上からj行目をひっくり返す
				for k := 0; k < c; k++ {
					if new_table[j][k] == 1 {
						new_table[j][k] = 0
					} else {
						new_table[j][k] = 1
					}
				}
			}
		}
		fmt.Println("-------")
		fmt.Printf("i = %v\n", i)
		for j := 0; j < r; j++ {
			fmt.Println(table[j])
		}
		// ひっくり返したやつを縦にみて、1の数がr/2より大きければひっくり返すに値する
		reverse_count := 0
		for j := 0; j < c; j++ {
			tmp_count := 0
			for k := 0; k < r; k++ {
				if new_table[k][j] == 1 {
					tmp_count += 1
				}
			}
			if tmp_count > r/2 {
				reverse_count += tmp_count
			}
		}
		ans = max(ans, reverse_count)
	}
	fmt.Fprintln(out, ans)
}

func max(a, b int) int {
	if a > b {
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
