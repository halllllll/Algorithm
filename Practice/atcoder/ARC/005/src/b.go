// いくらでも方法があるので好きなのを使え ぼくはゲームプログラミングっぽい感じにした
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var X, Y int
	var W string
	fmt.Scan(&X, &Y, &W)
	T := make([][]int, 9)
	for i := 0; i < 9; i++ {
		var line string
		T[i] = make([]int, 9)
		fmt.Scan(&line)
		for j, c := range []rune(line) {
			T[i][j], _ = strconv.Atoi(string(c))
		}
	}
	X--
	Y--
	ans := strconv.Itoa(T[Y][X])
	dx, dy := 0, 0
	switch W {
	case "R":
		dx = 1
	case "L":
		dx = -1
	case "U":
		dy = -1
	case "D":
		dy = 1
	case "RU":
		dx, dy = 1, -1
	case "RD":
		dx, dy = 1, 1
	case "LU":
		dx, dy = -1, -1
	case "LD":
		dx, dy = -1, 1
	}
	for i := 0; i < 3; i++ {
		if X+dx < 0 || 9 <= X+dx {
			dx *= -1
		}
		if Y+dy < 0 || 9 <= Y+dy {
			dy *= -1
		}
		X += dx
		Y += dy
		ans += strconv.Itoa(T[Y][X])
	}
	fmt.Println(ans)
}
