// 計６パターン？

package main

import "fmt"

func main() {
	var X, Y int
	fmt.Scan(&X, &Y)
	if X <= 0 && Y <= 0 {
		if Y < X {
			fmt.Println(min(1+abs(X)+abs(Y), 2+abs(abs(X)-abs(Y))))
		} else {
			fmt.Println(abs(abs(Y) - abs(X)))
		}
	} else if 0 <= X && 0 <= Y {
		if X <= Y {
			fmt.Println(Y - X)
		} else if Y < X {
			fmt.Println(min(Y+X+1, 2+abs(abs(Y)-abs(X))))
		}
	} else {
		fmt.Println(1 + abs(abs(Y)-abs(X)))
	}
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
