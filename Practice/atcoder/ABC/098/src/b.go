// きりみんちゃんの配信からきました
// こういう問題苦手（実装がめんどくさい）
// だるいので愚直でいいや
package main

import "fmt"

var n int
var s string

func main() {
	alphabets := []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
	fmt.Scan(&n, &s)
	ans := 0
	// 区切る場所で区切って左右のアルファベットの登場するか否かを数えて比較して両方にあったらインクリメントしてansと比較
	// あーだるい。。
	for i := 1; i < n-1; i++ {
		pre, epi := make(map[string]bool), make(map[string]bool)

		for j := 0; j < i; j++ {
			t := string([]rune(s)[j])
			if _, ok := pre[t]; !ok {
				pre[t] = true
			}
		}
		for j := i; j < n; j++ {
			t := string([]rune(s)[j])
			if _, ok := epi[t]; !ok {
				epi[t] = true
			}
		}
		tmp := 0
		for _, a := range alphabets {
			if pre[a] && epi[a] {
				tmp += 1
			}
		}
		ans = max(ans, tmp)
	}
	fmt.Println(ans)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
