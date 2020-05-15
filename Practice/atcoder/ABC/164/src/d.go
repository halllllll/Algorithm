// 勘 なにもかも勘
package main

import (
	"fmt"
	"strconv"
)

func main() {
	var S string
	fmt.Scan(&S)
	SS := make([]string, len(S))
	for i, c := range []rune(S) {
		SS[i] = string(c)
	}
	D := make(map[int]int)
	D[0] = 1 // ncrが失敗するので（？？？？？？？？？？？？？？？？？
	tmp := 0
	x10 := 1
	for i := len(SS) - 1; i >= 0; i-- {
		a, _ := strconv.Atoi(SS[i])
		tmp = (a*x10 + tmp)
		tmp %= 2019
		x10 *= 10
		x10 %= 2019
		D[tmp]++
	}
	ans := 0
	for _, v := range D {
		if v > 1 {
			ans += v * (v - 1) / 2
		}
	}
	fmt.Println(ans)
}
