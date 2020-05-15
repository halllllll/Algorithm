// やるだけだがこれ緑difなんすね
// N=M=1のときのアレでミスって1WA
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
	N, M := nextInt(), nextInt()
	A, T := make([][]string, N), make([][]string, M)
	for i := 0; i < N; i++ {
		A[i] = chars(next())
	}
	for i := 0; i < M; i++ {
		T[i] = chars(next())
	}
	if N == 1 && M == 1 {
		if A[0][0] == T[0][0] {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
		return
	}
	for i := 0; i < N-M; i++ {
		for j := 0; j < N-M; j++ {
			flag := true
			for y := 0; y < M; y++ {
				for x := 0; x < M; x++ {
					if A[i+y][j+x] != T[y][x] {
						flag = false
					}
				}
			}
			if flag {
				fmt.Fprintln(out, "Yes")
				return
			}
		}
	}
	fmt.Fprintln(out, "No")
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func chars(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
	}
	return ret
}
