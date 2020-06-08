// 1から足してってちょうどになったらそれ、越えたら超えたぶんをぬかしたそれ
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	sum := 0
	ans := make(map[int]bool)
	for i := 1; sum < N; i++ {
		sum += i
		ans[i] = true
	}
	if sum > N {
		ans[sum-N] = false
	}
	for k, v := range ans {
		if v {
			fmt.Println(k)
		}
	}
}
