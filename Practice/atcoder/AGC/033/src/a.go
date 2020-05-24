// 解説読んだ
// PythonだとTLEなりやがるので

package main

import "fmt"

type Grid struct {
	X, Y int
}

func main() {
	var H, W int
	fmt.Scan(&H, &W)
	T := make([][]bool, H)
	queue := []Grid{}
	for i := 0; i < H; i++ {
		var line string
		fmt.Scan(&line)
		T[i] = make([]bool, W)
		for j, c := range []rune(line) {
			if string(c) == "#" {
				T[i][j] = true
				queue = append(queue, Grid{X: j, Y: i})
			}
		}
	}
	steps := []int{0, 1, 0, -1, 0}
	ans := 0
	for len(queue) > 0 {
		nex_queue := []Grid{}
		for _, q := range queue {
			for i := 0; i < 4; i++ {
				nx, ny := q.X+steps[i], q.Y+steps[i+1]
				if 0 <= nx && nx < W && 0 <= ny && ny < H && !T[ny][nx] {
					T[ny][nx] = true
					nex_queue = append(nex_queue, Grid{X: nx, Y: ny})
				}
			}
		}
		queue = nex_queue
		ans++
	}
	fmt.Println(ans - 1)
}
