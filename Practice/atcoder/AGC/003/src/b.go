// iとi+1で少ないほうとったあと大きいほうを...と思ったけど合計してドレインしてもいいか
// 3 6 2 0 5 2 とかだと最初の2つをドレインすると [0 1 2 0 5 2]になる
// 残してもしょうがないので吸い尽くせ
// クソコーナーケースでWA
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N := nextInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = nextInt()
	}
	if N == 1 {
		fmt.Fprintln(out, A[0]/2)
		return
	}
	ans := 0
	for i := 1; i < N; i++ {
		sum := A[i] + A[i-1]
		if sum%2 == 0 {
			// 吸い尽くせ
			ans += sum / 2
			A[i], A[i-1] = 0, 0
		} else {
			ans += (sum - 1) / 2
			if A[i] != 0 {
				A[i] = 1
			}
			A[i-1] = 0
		}
	}
	fmt.Fprintln(out, ans)
}
func next() string {
	sc.Scan()
	return sc.Text()
}
func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}
func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}

// 10
// 1 8 3 4 2 1 4 6 0 4 3
// 1 0
