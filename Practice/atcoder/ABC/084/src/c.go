// 一回一回探索してもまあよさそう
// なぜか大量にWAをくらう あってるのはサンプルくらい 地獄
// lcm使ってたのが駄目っぽい（それはそう

package main

import "fmt"

type Data struct {
	C, S, F int
}

func main() {
	var N int
	fmt.Scan(&N)
	datas := make([]Data, N-1)
	for i := 0; i < N-1; i++ {
		var c, s, f int
		fmt.Scan(&c, &s, &f)
		datas[i] = Data{C: c, S: s, F: f}
	}
	for i := 0; i < N-1; i++ {
		time := datas[i].S + datas[i].C
		for j := i + 1; j < N-1; j++ {
			// ここについたときに経過してる時間 vs 次の出発
			// 出発前 -> 始発の時間にする
			// 出発済 -> 次のやつ
			if datas[j].S >= time {
				time = datas[j].S + datas[j].C
			} else {
				// いまの時間を超える最小のF
				x := (time / datas[j].F)
				if time%datas[j].F != 0 {
					x += 1
				}
				x *= datas[j].F
				time = x + datas[j].C
			}
		}
		fmt.Println(time)
	}
	fmt.Println(0)
}
