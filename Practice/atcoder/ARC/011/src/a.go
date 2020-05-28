// 制限がゆるいのでシミュ
package main

import "fmt"

func main() {
	var M, N, K int
	fmt.Scan(&M, &N, &K)
	ans := K
	cur := K
	for cur/M > 0 {
		ans += N * (cur / M)
		cur = N*(cur/M) + (cur % M)
	}
	fmt.Println(ans)
}
