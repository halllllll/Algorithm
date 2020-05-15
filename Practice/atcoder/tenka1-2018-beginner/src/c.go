package main

// 実験する 両端においていく？
// 最後のやつを先頭に付けるタイプとそのままのタイプで比較（なんでだろうね
// 6ケースでなぜかWA まじでなんでだろうね 意味不明
// じゃ先頭のやつを最後に付けるのも試す？

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	B := append([]int{}, A...)
	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	sort.Ints(B)
	s, t := []int{}, []int{}
	l, r := 0, N-1
	for l <= r {
		s = append(s, A[l])
		t = append(t, B[l])
		l++
		if l > r {
			break
		}
		s = append(s, A[r])
		t = append(t, B[r])
		r--
	}
	// 意味がわからんが先頭を末尾に/末尾を先頭にしたものを揃えてみる 意味は分からんが
	// なんかサンプルではans5かans6になりそうだがなぜなのかは不明
	ans1, ans2 := 0, 0
	for i := 1; i < N; i++ {
		ans1 += abs(s[i-1] - s[i])
		ans2 += abs(t[i-1] - t[i])
	}
	ans3 := ans1 - abs(s[0]-s[1]) + abs(s[0]-s[N-1])
	ans4 := ans2 - abs(t[0]-t[1]) + abs(t[0]-t[N-1])
	ans5 := ans1 - abs(s[N-2]-s[N-1]) + abs(s[0]-s[N-1])
	ans6 := ans2 - abs(t[N-2]-t[N-1]) + abs(t[0]-t[N-1])
	fmt.Println(max(ans1, max(ans2, max(ans3, max(ans4, max(ans5, ans6))))))
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}
