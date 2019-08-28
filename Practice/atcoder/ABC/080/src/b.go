package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	// 各桁をとるのにstrconvなんて要らねぇ
	cnt, tmp := 0, 0
	tmp = n
	for 0 < tmp {
		cnt += tmp % 10
		tmp /= 10
	}
	if n%cnt == 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
