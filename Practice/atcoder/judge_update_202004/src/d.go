package main

import "fmt"

// 累積gcdってなんですか....?
// いやなにかは分かったけどなんでそれ使えばいいんですか...?

func main() {
	var N, Q int
	fmt.Scan(&N, &Q)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var j int
		fmt.Scan(&j)
		A[i] = j
	}
	ruisekiGcd := make([]int, N)
	ruisekiGcd[0] = A[0]
	for i := 1; i < N; i++ {
		ruisekiGcd[i] = gcd(ruisekiGcd[i-1], A[i])
	}
	for i := 0; i < Q; i++ {
		var S int
		fmt.Scan(&S)
		// gcd()して1にならなかったらもうお前は駄目だ
		if x := gcd(S, ruisekiGcd[len(ruisekiGcd)-1]); x != 1 {
			fmt.Println(x)
			continue
		}
		l, r := 0, N
		for r-l > 0 {
			mid := (r + l) / 2
			if gcd(S, ruisekiGcd[mid]) > 1 {
				l = mid + 1
			} else {
				r = mid
			}
		}
		fmt.Println(l + 1)
	}
}

func gcd(a, b int) int {
	if a > b {
		a, b = b, a
	}
	for a > 0 {
		a, b = b%a, a
	}
	return b
}
