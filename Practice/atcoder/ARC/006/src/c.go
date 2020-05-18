// 頭からみて毎回どこに置くか決める、どこにも置けなかったら土台にして新しく山を作る
// Nが小さいので毎回ソートして更新したりしてもかまわなそう
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	ans := []int{}
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if i == 0 {
			ans = append(ans, V)
			continue
		}
		sort.Ints(ans)
		idx := sort.Search(len(ans), func(j int) bool {
			return ans[j] >= V
		})
		if idx == len(ans) {
			// 追加するしかなさそう
			ans = append(ans, V)
		} else {
			ans[idx] = V
		}
	}
	fmt.Println(len(ans))
}
