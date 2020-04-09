package main

import "fmt"

var table [][]string

type Pos struct {
	y, x int
}

func main() {
	var h, w int
	fmt.Scan(&h, &w)
	table = make([][]string, h)
	for i := 0; i < h; i++ {
		table[i] = make([]string, w)
		var m string
		fmt.Scan(&m)
		for j := 0; j < w; j++ {
			table[i][j] = string([]rune(m)[j])
		}
	}
	if table[0][0] == "." || table[h-1][w-1] == "." {
		fmt.Println("Impossible")
		return
	}
	queue := []Pos{}
	queue = append(queue, Pos{y: 0, x: 0})
	for len(queue) > 0 {
		var cur Pos
		cur, queue = queue[len(queue)-1], queue[:len(queue)-1]
		if cur.y == h-1 && cur.x == w-1 {
			table[cur.y][cur.x] = "."
			break
		}
		steps := []int{0, 1, 0}
		for i := 0; i < 2; i++ {
			next_y, next_x := cur.y+steps[i], cur.x+steps[i+1]
			if 0 <= next_y && next_y < h && 0 <= next_x && next_x < w {
				if table[next_y][next_x] == "#" {
					next_Pos := Pos{next_y, next_x}
					queue = append(queue, next_Pos)
					table[cur.y][cur.x] = "."
				}
			}
		}
	}
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			if table[y][x] == "#" {
				fmt.Println("Impossible")
				return
			}
		}
	}
	fmt.Println("Possible")

}
