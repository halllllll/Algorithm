// これむずいよね
// a + b + c = N 2a + 3b + 4c = Mとして
// M奇数ならbが奇数個必要になる
// できない条件is何
// とか考えるけどただの鶴亀
// O(1)むずい
package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	if M < 2*N || 4*N < M {
		fmt.Printf("%d %d %d\n", -1, -1, -1)
		return
	}
	if 3*N == M {
		fmt.Printf("%d %d %d\n", 0, N, 0)
	} else if 3*N > M {
		fmt.Printf("%d %d %d\n", 3*N-M, N-(3*N-M), 0)
	} else if 3*N < M {
		fmt.Printf("%d %d %d\n", 0, N-(M-3*N), M-3*N)
	}
}
