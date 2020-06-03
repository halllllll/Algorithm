// 最       悪      行列が逆だった 横が行ね...
// 1<=p<=N 1<=q<=Mとして p*(M-q)+q*(N-p)=黒
package main

import "fmt"

func main() {
	var N, M, K int
	fmt.Scan(&N, &M, &K)
	if N == 1 || M == 1 {
		fmt.Println("Yes")
		return
	}
	flag := false
	for p := 0; p <= N; p++ {
		for q := 0; q <= M; q++ {
			if p*(M-q)+q*(N-p) == K {
				flag = true
			}
		}
	}
	if flag {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
