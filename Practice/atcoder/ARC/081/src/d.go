// ていねいにやる 前回の情報を覚えておく
// 初期値で一瞬混乱した
package main

import "fmt"

func main() {
	var N int
	var S1, S2 string
	fmt.Scan(&N, &S1, &S2)
	S, T := make([]string, N), make([]string, N)
	for i, c := range []rune(S1) {
		S[i] = string(c)
	}
	for i, c := range []rune(S2) {
		T[i] = string(c)
	}
	MOD := int(1e9) + 7
	pre := -1 // 0..縦*1 1..横*2
	ans := -1
	idx := -1
	if S[0] == T[0] {
		pre = 0
		idx = 1
		ans = 3
	} else {
		pre = 1
		idx = 2
		ans = 6
	}
	for idx < N {
		if pre == 0 {
			if S[idx] == T[idx] {
				ans *= 2
				idx++
			} else {
				pre = 1
				ans *= 2
				idx += 2
			}
		} else {
			if S[idx] == T[idx] {
				pre = 0
				idx++
			} else {
				// aa								bb    bb		 cc
				// bb	の横に並べるのは cc or aa or  aa の3種類
				ans *= 3
				idx += 2
			}
		}
		ans %= MOD
	}
	fmt.Println(ans)
}
