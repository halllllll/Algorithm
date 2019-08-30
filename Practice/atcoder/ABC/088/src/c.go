package main

import (
	"fmt"
)

var table = make([][]int, 3)

func main() {
	for i := 0; i < 3; i++ {
		column := make([]int, 3)
		var a, b, c int
		fmt.Scan(&a, &b, &c)
		column[0], column[1], column[2] = a, b, c
		table[i] = column
	}
	// 縦, 横
	var a1, a2, a3, b1, b2, b3 int
	ans := false
	// 0<=as[0]<=100として調べる
	for ; a1 <= 100; a1++ {
		b1 = table[0][0] - a1
		b2 = table[0][1] - a1
		b3 = table[0][2] - a1
		a2 = table[1][0] - b1
		a3 = table[2][0] - b1
		if a2+b2 == table[1][1] && a2+b3 == table[1][2] && a3+b2 == table[2][1] && a3+b3 == table[2][2] {
			ans = true
			break
		}
	}
	if ans {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}

}
