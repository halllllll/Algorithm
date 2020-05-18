package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	P, Q := make([]int, N), make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&P[i])
	}
	for i := 0; i < N; i++ {
		fmt.Scan(&Q[i])
	}
	arr := make([]int, N)
	for i := 1; i <= N; i++ {
		arr[i-1] = i
	}
	np := next_permutation(arr)
	a, b := 0, 0
	i := 1
	for {
		lis := np()
		if len(lis) == 0 {
			break
		}
		if a == 0 {
			flagP := true
			for j := 0; j < N; j++ {
				if lis[j] != P[j] {
					flagP = false
				}
			}
			if flagP {
				a = i
			}
		}
		if b == 0 {
			flagQ := true
			for j := 0; j < N; j++ {
				if lis[j] != Q[j] {
					flagQ = false
				}
			}
			if flagQ {
				b = i
			}
		}
		i++
	}
	fmt.Println(abs(a - b))
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}

func next_permutation(arr []int) func() []int {
	ret := append([]int{}, arr...)
	_next_permutation := func() []int {
		n := len(ret)
		for i := n - 2; i >= 0; i-- {
			if ret[i] < ret[i+1] {
				j := n
				for {
					j -= 1
					if ret[i] < ret[j] {
						break
					}
				}
				ret[i], ret[j] = ret[j], ret[i]
				for k := n - 1; i < k; i, k = i+1, k-1 {
					ret[i+1], ret[k] = ret[k], ret[i+1]
				}
				return ret
			}
		}
		return []int{}
	}
	return _next_permutation
}
