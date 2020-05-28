// 相変わらず文章がぜんぜん頭にはいってこんな
// スイッチの状態を全探索る -> そのあとの判定が毎回混乱する
package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	T := make([][]bool, M)
	for i := 0; i < M; i++ {
		var K int
		fmt.Scan(&K)
		T[i] = make([]bool, N)
		for j := 0; j < K; j++ {
			var V int
			fmt.Scan(&V)
			T[i][V-1] = true
		}
	}
	P := make([]int, M)
	for i := 0; i < M; i++ {
		fmt.Scan(&P[i])
	}
	ans := 0
	for bit := 0; bit < (1 << uint(N)); bit++ {
		tmp := []int{}
		for i := 0; i < N; i++ {
			if (bit>>uint(i))&1 == 1 {
				tmp = append(tmp, i)
			}
		}
		// スイッチの状態がtmp=onであったときそれぞれの電球がついてるかどうか これ
		flag := true
		for i := 0; i < M; i++ {
			yo := 0 // onになってるスイッチの数
			for _, t := range tmp {
				if T[i][t] {
					yo++
				}
			}
			// 判定
			if P[i] != yo%2 {
				flag = false
			}
		}
		if flag {
			ans++
		}
	}
	fmt.Println(ans)
}
