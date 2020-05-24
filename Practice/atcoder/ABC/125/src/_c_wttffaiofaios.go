// ????
// Nが3以上素数が2つ以上あったら強制的に1になるので約数が関係してくる（それはそう）
// 素因数分解してsetをとっていく感じ、途中該当しないのがきたら1回だけチャンスを与えてやる
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	sort.Ints(A)

	chance := true
	set := primeFactorization(A[0])
	for i := 0; i < N; i++ {
		divs := primeFactorization(A[i])
		tmp := make(map[int]int)
		for k, v := range set {
			if _, ok := divs[k]; ok {
				tmp[k] = min(v, divs[k])
			}
		}
		if len(tmp) < len(set) && chance {
			chance = false
		} else {
			set = tmp
		}
	}
	ans := 1
	for k, v := range set {
		ans *= pow(k, v)
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func primeFactorization(x int) map[int]int {
	ret := make(map[int]int)
	for i := 2; i*i <= x; i++ {
		for x%i == 0 {
			x /= i
			ret[i] += 1
		}
	}
	if x > 1 {
		ret[x] += 1
	}
	return ret
}

func pow(a, x int) int {
	if x == 0 {
		return 1
	}
	tmp := 1
	for i := 0; i < x; i++ {
		tmp *= a
	}
	return tmp
}
