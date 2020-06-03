// 明らかに最大のやつに引っ張られる
// それ以外のやつは最大のやつの合間にはさめばいいので、max(A)-1<=max(A)以外の合計、ならばいける
// いけない場合はmax(A)-1-max(A)以外の合計かな
package main

import "fmt"

var k, t int

func main() {
	fmt.Scan(&k, &t)
	max_a := -1
	for i := 0; i < t; i++ {
		var j int
		fmt.Scan(&j)
		if j > max_a {
			max_a = j
		}
	}
	sum := k - max_a
	if max_a-1 <= sum {
		fmt.Println(0)
	} else {
		fmt.Println(max_a - 1 - sum)
	}
}
