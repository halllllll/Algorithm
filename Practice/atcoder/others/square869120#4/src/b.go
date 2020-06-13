// 2^15は余裕で間に合う 選んだやつを単調増加するが、それぞれの間に高いやつがないように味付けする
// たぶんKぴったりでいい気がする（超える必要はない）（答えるのはかかったコストなので）
package main

import "fmt"

func main() {
	var N, K int
	fmt.Scan(&N, &K)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	ans := int(1e18)
	for bit := 0; bit < (1 << uint64(N)); bit++ {
		tmp := make([]bool, N)
		count := 0
		for i := 0; i < N; i++ {
			if (bit>>uint64(i))&1 == 1 {
				tmp[i] = true
				count++
			}
		}
		if count != K {
			continue
		}
		pre, cost := -1, 0
		B := append([]int{}, A...)
		for i, f := range tmp {
			if f {
				if pre >= B[i] {
					cost += pre - B[i] + 1
					B[i] += pre - B[i] + 1
				}
				pre = B[i]
			} else {
				pre = max(pre, B[i])
			}
		}
		ans = min(ans, cost)
	}
	if K == 1 {
		fmt.Println(0)
		return
	}
	fmt.Println(ans)
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
