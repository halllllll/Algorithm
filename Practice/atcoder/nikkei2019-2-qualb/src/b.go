// 問題文の意味はわからんがサンプルを眺めてて浮かんだ
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	MOD := 998244353
	D := make(map[int]int)
	maxN := 0
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		// 最初必ず0なので
		if i == 0 && V != 0 {
			fmt.Println(0)
			return
		}
		D[V]++
		maxN = max(maxN, V)
	}
	// 0はひとつ
	if D[0] > 1 {
		fmt.Println(0)
		return
	}
	// 順番を飛ばしていたら存在しなさそう
	for i := 0; i <= maxN; i++ {
		if _, ok := D[i]; !ok {
			fmt.Println(0)
			return
		}
	}
	// はい やっと本質
	keys := []int{}
	for k := range D {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	ans := 1
	for i := 1; i < len(keys); i++ {
		ans = ans * powMod(D[i-1], D[i], MOD)
		ans %= MOD
	}
	fmt.Println(ans)
}

func powMod(n, m, mod int) (ret int) {
	ret = 1
	for m > 0 {
		if m&1 == 1 {
			ret *= n
			ret %= mod
		}
		n *= n
		n %= mod
		m >>= 1
	}
	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
