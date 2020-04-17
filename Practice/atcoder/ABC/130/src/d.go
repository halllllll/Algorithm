// バチャからきました https://kenkoooo.com/atcoder/#/contest/show/811225d0-fa06-4ddb-ba30-5b180f7bff6d
// しゃくとり
package main
import "fmt"
func main(){
	var N ,K int
	fmt.Scan(&N, &K)
	A := make([]int, N+1)
	for i:=0; i<N; i++{
		var j int
		fmt.Scan(&j)
		A[i] = j
	}
	A = append(A, 0)
	r := 0
	tmp := 0
	ans := 0
	// 条件を満たさない限り続けて、満たしたら抜ける
	for l:=0; l<N; l++{
		for r < N && tmp < K{
			tmp += A[r]
			r += 1
		}
		if tmp >= K{
			ans += N-(r-1)
		}
		tmp -= A[l]
		if r < l{
			r = l
		}
	}
	fmt.Println(ans)
}