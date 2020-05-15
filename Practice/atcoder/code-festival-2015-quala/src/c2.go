// Aだけで完結できるならそうするができなかった場合にBから置き換える
// 置き換えるやつはできるだけ効果の高いのがいい つまり置き換えることによって下げ幅がデカいやつほど優先的にする
// カウントを数えて合格したら終了
// インデックス保持したままソートしなきゃいけないんじゃね？とか勘違いしたけど差のぶん減るだけでインデックスの情報必要なかったわ
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N, T int
	fmt.Scan(&N, &T)
	s := 0
	fuck := 0 // なぜか最後に判断できなくて2WA食らってキレたのでこうする こうじゃ
	Dif := make([]int, N)
	for i := 0; i < N; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		fuck += a - b
		Dif[i] = a - b
		s += a
	}
	// こうじゃ 俺は好きにした お前らも好きにしろ
	if s-fuck > T {
		fmt.Println(-1)
		return
	}
	sort.Sort(sort.Reverse(sort.IntSlice(Dif)))
	ans := 0
	idx := 0
	for s > T && idx < N {
		s -= Dif[idx]
		ans++
		idx++
	}
	// 好きにしたのでこれは必要なかろう つかなんでこれが駄目なんだろうね💢
	// if idx >= N || s > T {
	// 	fmt.Println(-1)
	// } else {
	// 	fmt.Println(ans)
	// }
	fmt.Println(ans)
}
