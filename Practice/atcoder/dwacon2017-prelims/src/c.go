// シミュ
// 問題文を誤読していた 順番じゃなくていいのかよ
// シミュするのしんどいなんかいい方法ないか
// 3は1としかペアになれんので優先的に潰す
// 無駄に時間かかったわりに学びがない

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	M := make(map[int]int)
	M[1], M[2], M[3], M[4] = 0, 0, 0, 0
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
		M[V]++
	}
	ans := 0
	if M[1] > 0 && M[3] > 0 {
		t := min(M[1], M[3])
		ans += t
		M[1] -= t
		M[3] -= t
	}
	if M[3] > 0 {
		ans += M[3]
	}
	// もう3には用ない

	// 2を2同士で潰す
	if M[2] >= 2 {
		ans += M[2] / 2
		M[2] %= 2
	}
	// 1と2で4を作れるだけ作る
	if M[2] >= 1 && M[1] >= 2 {
		t := min(M[2], M[1]/2)
		M[2] -= t
		M[1] -= 2 * t
		ans += t
	}

	if M[2] > 0 && M[1] > 0 {
		// 3しかつくれない（はず）
		ans += 1
		M[2] = 0
		M[1] = 0
	} else if M[2] == 0 && M[1]%4 == 0 {
		ans += M[1] / 4
	} else if M[2] == 0 {
		ans += M[1]/4 + 1
		M[1] = 0
	}
	// これありえるか？
	if M[2] > 0 {
		if M[2]%2 == 0 {
			ans += M[2] / 2
		} else {
			ans += M[2]/2 + 1
		}
	}
	// 4はそのまんま
	ans += M[4]
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// 6
// 3
// 3
// 2
// 1
// 1
// 1

// 3になってほしいが4になっちゃった
