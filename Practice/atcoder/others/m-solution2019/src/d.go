// 一番でかいやつを排除したのが合計値になりそう->端っこに入れる
// 合計がsum(arr)-max(arr)を目指すので適当に↑の続きから大きい順に入れていけば、いれたやつが採用されそう
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	T := make([][]int, N)
	for i := 0; i < N; i++ {
		T[i] = []int{}
	}
	for i := 0; i < N-1; i++ {
		var A, B int
		fmt.Scan(&A, &B)
		T[A-1] = append(T[A-1], B-1)
		T[B-1] = append(T[B-1], A-1)
	}
	C := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&C[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(C)))
	start := -1
	for i, t := range T {
		if len(t) == 1 {
			start = i
			break
		}
	}
	ans := 0
	queue := []int{start}
	used := make([]int, N)
	idx := 0
	used[start] = C[idx]
	for len(queue) > 0 {
		cur := queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		for _, t := range T[cur] {
			if used[t] == 0 {
				idx++
				used[t] = C[idx]
				ans += C[idx]
				queue = append(queue, t)
			}
		}
	}
	fmt.Println(ans)
	for _, p := range used {
		fmt.Printf("%d ", p) // atcoderこれでも許された気がする
	}
}
