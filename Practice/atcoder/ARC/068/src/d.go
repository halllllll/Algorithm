// 3以上あるやつはオナニーすれば奇数だと1枚 偶数だと2枚にできる
// 2が偶数枚 -> 全部とれそう
// 奇数枚 -> 1枚減りそう
// なんでそうなるかの考察は不明
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	M := make(map[int]int)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		M[V]++
	}
	MM := make(map[int]int)
	for k, v := range M {
		if v >= 3 {
			if v%2 == 1 {
				MM[k] = 1
			} else {
				MM[k] = 2
			}
		} else {
			MM[k] = v
		}
	}
	count := 0
	for _, v := range MM {
		if v == 2 {
			count++
		}
	}
	if count%2 == 0 {
		fmt.Println(len(MM))
	} else {
		fmt.Println(len(MM) - 1)
	}
}
