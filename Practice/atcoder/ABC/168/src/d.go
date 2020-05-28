// 1からスタンプを押していくBFS
// golangでpriority queueもってないから愚直FIFOで間に合うかどうかは正直わからん
// ちょっとだけIOを高速化したバージョン
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Pos struct {
	cur, pre int
}

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N, M := nextInt(), nextInt()

	T := make([][]int, N+1)
	for i := 1; i <= N; i++ {
		T[i] = []int{}
	}
	for i := 0; i < M; i++ {
		A, B := nextInt(), nextInt()
		T[A] = append(T[A], B)
		T[B] = append(T[B], A)
	}
	passed := make([]int, N+1)
	passed[1] = -1
	queue := []Pos{Pos{cur: 1, pre: 0}}
	for len(queue) > 0 {
		nex_queue := []Pos{}
		for i := 0; i < len(queue); i++ {
			now := queue[i]
			for _, nex := range T[now.cur] {
				if passed[nex] == 0 {
					nexPos := Pos{cur: nex, pre: now.cur}
					passed[nex] = now.cur
					nex_queue = append(nex_queue, nexPos)
				}
			}
		}
		queue = nex_queue
	}
	fmt.Fprintln(out, "Yes")
	for _, ans := range passed[2:] {
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
