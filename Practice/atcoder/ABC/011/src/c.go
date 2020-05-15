// dpぽい Nが小さいが用意しておく
// 以前のAC提出をみたら思いつかんかったことやってて賢い 大きい順なるほど
package main

import "fmt"

var N, NG1, NG2, NG3 int
var DP map[int]map[int]bool

func main() {
	fmt.Scan(&N, &NG1, &NG2, &NG3)
	DP = make(map[int]map[int]bool)
	if rec(100, N) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}

func rec(i, cur int) bool {
	if _, ok := DP[i]; ok {
		if _, ok2 := DP[i][cur]; ok2 {
			return DP[i][cur]
		}
	}
	if cur == NG1 || cur == NG2 || cur == NG3 {
		return false
	}
	if cur == 0 {
		return true
	}
	if i <= 0 {
		return false
	}
	ret := rec(i-1, cur-1) || rec(i-1, cur-2) || rec(i-1, cur-3)
	if _, ok := DP[i]; !ok {
		DP[i] = make(map[int]bool)
	}
	DP[i][cur] = ret
	return ret
}
