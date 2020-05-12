// dp典型
package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	S := make([]int, N+1)
	T := make([]bool, N+1)
	MOD := int(10e8) + 7
	if M > 0 {
		// panic("は？？？？？？なにこれ こんなことして楽しいの？？")
		for i := 0; i < M; i++ {
			var V int
			fmt.Scan(&V)
			T[V] = true // 直感と反してわかりにくいがtrueが踏んじゃ駄目なつもり
		}
	}
	// 初期化
	if N >= 1 {
		S[0] = 1
		if !T[1] {
			S[1] = 1
		}
	}
	if N >= 2 {
		if !T[2] {
			S[2] = S[1] + 1
		}
	}

	// 探索
	for i := 3; i < N+1; i++ {
		if T[i] {
			S[i] = 0
		} else {
			S[i] = S[i-1] + S[i-2]
			S[i] %= MOD
		}
	}
	fmt.Println(S[len(S)-1])
}
