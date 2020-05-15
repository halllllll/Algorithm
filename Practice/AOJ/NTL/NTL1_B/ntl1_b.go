// 繰り返し二乗法
package main

import "fmt"

func main() {
	var M, N int
	fmt.Scan(&M, &N)
	MOD := int(1e9) + 7
	fmt.Println(expSqrMod(M, N, MOD))
}

// 非再帰ver
func expSqrMod(n, m, mod int) int {
	ret := 1
	n %= mod
	for m > 0 {
		fmt.Printf("now n ret : %d %d\n", n, ret)
		if m&1 == 1 {
			fmt.Println("ret更新")
			ret = (ret * n) % mod
		}
		m = m >> 1
		n = (n * n) % mod
	}
	return ret
}
