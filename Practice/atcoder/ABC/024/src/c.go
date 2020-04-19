// Kiについて毎回やっても間に合うだろ多分
package main

import "fmt"

func main() {
	var N, D, K int
	fmt.Scan(&N, &D, &K)
	partitions := make([][]int, D)
	for i := 0; i < D; i++ {
		partitions[i] = make([]int, 2)
		var l, r int
		fmt.Scan(&l, &r)
		partitions[i][0], partitions[i][1] = l, r
	}
	for i := 0; i < K; i++ {
		var S, T int
		fmt.Scan(&S, &T)
		ans := 0
		for _, p := range partitions {
			ans += 1
			if p[0] <= S && S <= p[1] {
				if S < T && T <= p[1] {
					fmt.Println(ans)
					break
				} else if S < T {
					S = p[1]
				} else if S > T && T >= p[0] {
					fmt.Println(ans)
					break
				} else if S > T {
					S = p[0]
				}
			}
		}
	}
}
