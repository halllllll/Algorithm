// 典型BFS 最短パスと既存の#を引いたところ以外を#に塗るとしてその数
// たどりつけない場合を読み飛ばしてた...

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Pos struct {
	Y, X int
}

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	blacks := 0
	H, W := nextInt(), nextInt()
	T := make([][]int, H)
	for i := 0; i < H; i++ {
		T[i] = make([]int, W)
		line := chars(next())
		for j, c := range line {
			if c == "#" {
				T[i][j] = -1
				blacks++
			}
		}
	}
	T[0][0] = 1
	queue := []Pos{Pos{Y: 0, X: 0}}
	steps := []int{0, 1, 0, -1, 0}
	for len(queue) > 0 {
		nex_queue := []Pos{}
		for _, q := range queue {
			for i := 0; i < 4; i++ {
				ny, nx := q.Y+steps[i], q.X+steps[i+1]
				if 0 <= ny && ny < H && 0 <= nx && nx < W && T[ny][nx] == 0 {
					nexPos := Pos{Y: ny, X: nx}
					T[ny][nx] = T[q.Y][q.X] + 1
					nex_queue = append(nex_queue, nexPos)
				}
			}
		}
		queue = nex_queue
	}
	if T[H-1][W-1] == 0 {
		fmt.Fprintln(out, -1)
	} else {
		fmt.Fprintln(out, H*W-T[H-1][W-1]-blacks)
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

func nextStrings(n int) []string {
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		ret[i] = next()
	}
	return ret
}

func chars(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
	}
	return ret
}
