// 範囲でソートして真ん中がいけそうな気がしますが
// （必要なのはminとmidとmaxの3つで答えがmidの範囲だけなので）
// 偶数の場合の範囲の合体、かぶる場合に気づけず
// ↑結局この考えは駄目でした（なんでだろうね

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type D struct {
	a, b, dif int
}

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!caution!!!! you must use Fprint(out, ) not Print()
	N := nextInt()
	ds := make([]D, N)
	for i := 0; i < N; i++ {
		A, B := nextInt(), nextInt()
		ds[i] = D{a: A, b: B, dif: B - A}
	}
	sort.Slice(ds, func(i, j int) bool {
		return ds[i].dif < ds[j].dif
	})
	if N%2 == 0 {
		// 範囲を合体させる
		if ds[N/2].b < ds[N/2-1].a {
			fmt.Fprintln(out, ds[N/2].b-ds[N/2-1].a+1)
		} else {
			fmt.Fprintln(out, ds[N/2].dif+ds[N/2-1].dif+1)
		}
	} else {
		fmt.Fprintln(out, ds[N/2].dif+1)
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
