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
	A := nextInts(N)
	for _, X := range nextInts(Q) {
		ans, curSum, r := 0, 0, 0
		for l := 0; l < N; {
			for ; r < N && curSum+A[r] <= X; r++ {
				curSum += A[r]
			}
			if r-l > 0 {
				ans += r - l
				curSum -= A[l]
			}
			if r == l {
				r++
			}
			l++
		}
		fmt.Fprintln(out, ans)
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

func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}
