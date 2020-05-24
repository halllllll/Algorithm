// 愚直DFSでいけんの？ -> どう考えても駄目です
// 解説観て実装しただけなので理解がカスです あとでやれたらやります

package main

import "fmt"

func main() {
	var N, X, Y int
	fmt.Scan(&N, &X, &Y)
	ANS := make(map[int]int)
	for i := 1; i <= N; i++ {
		for j := i; j <= N; j++ {
			tmp := min(abs(i-j), min(abs(X-i)+abs(Y-j)+1, abs(X-j)+abs(Y-i)+1))
			ANS[tmp]++
		}
	}
	for i := 1; i < N; i++ {
		fmt.Println(ANS[i])
	}
}

func abs(a int) int {
	if a < 0 {
		a *= -1
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
