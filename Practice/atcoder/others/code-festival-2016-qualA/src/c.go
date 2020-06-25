// Sの長さは変わらないんので26進数で加算して繰り上げていくみたいなのはダメ
// 上の桁からできるだけ小さくしていくことを考える
// ↑手元でためしたときにアルファベットと数値の対応がおかしくてバグらせてることに気づかず解説みるという最悪をした

package main

import (
	"fmt"
	"strings"
)

func main() {
	var S string
	var K int
	fmt.Scan(&S, &K)
	char := "a"
	T := make(map[string]int)
	T[char] = 0
	for i := 1; i < 26; i++ {
		char = string(char[0] + 1)
		T[char] = 26 - i
	}
	ans := make([]string, len(S))
	for i, c := range []rune(S) {
		if T[string(c)] <= K {
			K -= T[string(c)]
			ans[i] = "a"
		} else {
			ans[i] = string(c)
		}
	}

	if K > 0 {
		K %= 26
		for i := 0; i < K; i++ {
			ans[len(S)-1] = string(ans[len(S)-1][0] + 1)
		}
	}
	fmt.Println(strings.Join(ans, ""))
}
