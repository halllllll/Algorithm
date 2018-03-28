package main

import (
	"fmt"
)

// strconv使ってstringにしてreverseにしようかと思ったけど結局スライスにバラして作り直すってのやんなきゃならんらしいので使わない

func check(n int) int {
	// 5桁は確定
	rev, tmp := 0, n
	for i := 10000; 0 < i; i /= 10 {
		rev += i * (tmp % 10)
		tmp /= 10
	}
	if rev == n {
		return 1
	} else {
		return 0
	}
}

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	ans := 0
	for i := a; i <= b; i++ {
		ans += check(i)
	}
	fmt.Println(ans)
}
