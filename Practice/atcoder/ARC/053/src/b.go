// 回数が奇数で低いものに引っ張られる 偶数で余裕のあるやつを均等に割り振る
package main

import "fmt"

func main() {
	var S string
	D := make(map[string]int)
	fmt.Scan(&S)
	for _, c := range []rune(S) {
		if _, ok := D[string(c)]; ok {
			D[string(c)] += 1
		} else {
			D[string(c)] = 1
		}
	}
	lowest_appeared_count := 0 // 1回しかでてこないやつ
	redudency_count := 0       // 使えるやつ 2以上の数で2で割ったもの
	for _, v := range D {
		if v == 0 {
			lowest_appeared_count += 1
		} else {
			if v%2 == 1 {
				lowest_appeared_count += 1
			}
			redudency_count += v / 2
		}
	}
	if lowest_appeared_count == 0 {
		// ぜんぶくっつけることができる
		fmt.Println(redudency_count * 2)
		return
	}
	ans := (redudency_count/lowest_appeared_count)*2 + 1
	fmt.Println(ans)
	// abcdddeeeeffgghhhh
	// 1つだけ: a b c d
	// その周りに足せるやつの総数 d*2 e*4 f*2 g*2 h*4 = 14
	// 実際は2つで1組なので7、これを割り振るのでたとえば dad eebee fgcgf hhdhhで3
}
