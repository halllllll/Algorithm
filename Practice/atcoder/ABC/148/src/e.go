// さんすう要素にビビるも問題文読んで「つまり2ずつ減ってくのか...?」となりサンプルを見てそのとおりだったのでN*(N-2)の下の桁が0になる条件を考える
// 登場した10と(2,5)の数に限られる気がする 奇数はまず無理
// 後者は無理 差が2なので
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	if N%2 == 1 || N < 10 {
		fmt.Println(0)
		return
	}
	T := []int{10}
	for i := 1; i < 18; i++ {
		T = append(T, T[len(T)-1]*10)
	}
	ans := 0
	for N > 0 {
		for i, t := range T {
			ans += N / t
			ans -= T[i]
		}
		N /= 10
	}
	fmt.Println(ans)
}
