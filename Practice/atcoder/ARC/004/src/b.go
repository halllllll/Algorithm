package main

import "fmt"

func main() {
	// ぜんぜん推敲してないけど最大距離は直線にならべたもので、最小距離は戻ってこれるならどんな手を使っても戻ってくるほうがいい
	// 戻ってこれない場合は最大値が総数から最大値を引いたものより長い場合 そんときゃ「最大値分進んで残りの総数ぶん戻る」をする
	var n int
	fmt.Scan(&n)
	max_n := -1
	sum := 0
	for i := 0; i < n; i++ {
		var j int
		fmt.Scan(&j)
		sum += j
		if j > max_n {
			max_n = j
		}
	}
	if n == 1 {
		fmt.Println(sum)
		fmt.Println(sum)
		return
	}
	if sum-max_n < max_n {
		fmt.Println(sum)
		fmt.Println(max_n - (sum - max_n))
	} else {
		fmt.Println(sum)
		fmt.Println(0)
	}
}
