// 左から順番にみていくとして、i=1からスタートすると
// i-1よりもiを優先的に犠牲にしたほうがいい
// （i+1にも影響を与えてくれるので）
// 1. A[i] + A[i-1] <= x -> そのまま
// 2. 1以外:
//			2.1. A[i] >=x -> A[i]だけ必要なぶん犠牲にして減らす
//			2.2 2.1以外 -> A[i-1]も犠牲にする
// *加算されるぶんはどちらも同じ
package main

import "fmt"

func main() {
	var N, X int
	fmt.Scan(&N, &X)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	ans := 0
	for i := 1; i < N; i++ {
		if A[i-1]+A[i] <= X {
			continue
		} else {
			hikubun := (A[i] + A[i-1]) - X
			ans += hikubun
			if A[i] >= hikubun {
				A[i] -= hikubun
			} else {
				// A[i-1]も減るけどどうせ今後登場しないので無視
				A[i] = 0
			}
		}
	}
	fmt.Println(ans)
}
