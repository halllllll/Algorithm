package main

import "fmt"

func main() {
	var N, K int
	MOD := 1000000000 + 7
	fmt.Scan(&N, &K)
	// N+1=4, 4c2+4c3+4c4 = 6+4+1
	// MaxとMinの差っぽい（1ずつだとその間のやつの種類は作れるので）
	ans := 1
	for i := K; i < N+1; i++ {
		min_d := i * (i + 1) / 2
		// fmt.Printf("maxの初項は %d\n", N+2-i)
		max_d := i * (2*(N+2-i) + (i - 1)) / 2
		// fmt.Println(min_d, max_d)
		ans += max_d - min_d + 1
		ans %= MOD
	}
	fmt.Println(ans)
}
