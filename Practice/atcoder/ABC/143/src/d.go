package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	L := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		L[i] = V
	}
	sort.Ints(L)
	ans := 0
	for a := 0; a < N-2; a++ {
		for b := a + 1; b < N-1; b++ {
			// なぜか以下うまくいかない 意味不明 わけわからん 2時間くらい無駄にした
			// from := sort.Search(N, func(j int) bool {
			// 	if a == 0 && b == 1 {
			// 		fmt.Printf("L[%d]+L[%d]=%d+%d > L[j] = L[%d]= %d????\n", a, b, L[a], L[b], j, L[j])
			// 	}
			// 	return j > b && L[a]+L[b] > L[j]
			// })
			// したかないのでスクラッチ
			l, r := b, N
			for r > l {
				mid := (l + r) / 2
				if L[a]+L[b] > L[mid] {
					l = mid + 1
				} else {
					r = mid
				}
			}
			if l > b {
				// fmt.Printf("L[%d]+L[%d]=%dを初めて下回るのはL[%d]=%d までの %d 個\n", a, b, L[a]+L[b], l-1, L[l-1], (l-1)-b)
				ans += (l - 1 - b)
			}
		}
	}
	fmt.Println(ans)
}
