// 余計なコメントがあったので削除（ABC088Dのbfsコピペして体裁整えただけだからね
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

	R, C := nextInt(), nextInt()
	Sy, Sx := nextInt(), nextInt()
	Gy, Gx := nextInt(), nextInt()

	T := make([][]int, R)
	for i := 0; i < R; i++ {
		T[i] = make([]int, C)
		line := chars(next())
		for j, c := range line {
			if c == "#" {
				T[i][j] = -1
			}
		}
	}
	queue := []Pos{Pos{Y: Sy - 1, X: Sx - 1}}
	steps := []int{0, 1, 0, -1, 0}
	for len(queue) > 0 {
		nex_queue := []Pos{}
		for _, q := range queue {
			for i := 0; i < 4; i++ {
				ny, nx := q.Y+steps[i], q.X+steps[i+1]
				if T[ny][nx] == 0 {
					nexPos := Pos{Y: ny, X: nx}
					T[ny][nx] = T[q.Y][q.X] + 1
					nex_queue = append(nex_queue, nexPos)
				}
			}
		}
		queue = nex_queue
	}
	fmt.Println(T[Gy-1][Gx-1])
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
