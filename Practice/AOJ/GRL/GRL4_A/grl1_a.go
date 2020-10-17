package main

import "fmt"

func main() {
	var V, E int
	fmt.Scan(&V, &E)
	T := make([][]int, V)
	for i := 0; i < V; i++ {
		T[i] = []int{}
	}
	for i := 0; i < E; i++ {
		var s, t int
		fmt.Scan(A, &t)
		T[s] = append(T[s], t)
		// T[t] = append(T[t], s) おいおいおいおいおい とんだ悪問ですわ 有向グラフだった
	}
	fmt.Println(T)
}
