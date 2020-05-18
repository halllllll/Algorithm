// 7以上が出るまでの累積和は
// 1 3 6 10 でi=4 それ以下のはどうとでも構築できる
// つかそう思えばビットが立ってるとこだけでいい気がするが
// -> そんなことありませんでした
// 予め10^7以下となるまでの累積和を用意して大きい順？にひいていく？
// ちがうわ 累積したらそこまでに不要なのが1つだけ出てくる...
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	idx := 1
	tmp := 1
	ruisekis := []int{idx}
	for tmp < N {
		idx++
		tmp += idx
		ruisekis = append(ruisekis, idx)
	}
	for _, a := range ruisekis {
		if a != tmp-N {
			fmt.Println(a)
		}
	}
}
