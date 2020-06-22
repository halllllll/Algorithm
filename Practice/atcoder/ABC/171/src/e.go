// 理屈はしらんけど全部のxorからA[i]のxorをとるとなんか答えがでた

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
	A := nextInts64(N)
	xor := A[0]
	for i := 1; i < N; i++ {
		xor = xor ^ A[i]
	}
	for _, a := range A {
		fmt.Fprintf(out, "%d ", xor^a)
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

func nextInts64(n int) []int64 {
	ret := make([]int64, n)
	for i := 0; i < n; i++ {
		ret[i] = int64(nextInt())
	}
	return ret
}
