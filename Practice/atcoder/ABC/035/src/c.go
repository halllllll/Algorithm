// 奇数回だと白 クエリが多いのでいもす
// ギリギリいけるかなーと思ったけどやっぱ通常のI/OだとTLEなる 高速化ライブラリ使う

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
	N, Q := nextInt(), nextInt()
	O := make([]int, N+10)
	for i := 0; i < Q; i++ {
		L, R := nextInt(), nextInt()
		O[L] += 1
		O[R+1] -= 1
	}
	ANS := make([]int, N)
	for i := 1; i <= N; i++ {
		O[i] += O[i-1]
		O[i] %= 2
		ANS[i-1] = abs(O[i] % 2)
	}
	for _, a := range ANS {
		fmt.Fprint(out, a)
	}
	// なんかちゃんと改行せにゃならん？
	fmt.Fprintln(out)
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}
