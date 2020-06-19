package main
import "fmt"
func main(){
	var N int
	fmt.Scan(&N)
	T := make([][]int, N)
	D := make([][]int, N+1)	// 累積和用テーブル
	for i:=0; i<=N; i++{
		D[i] = make([]int, N+1)
	}
	for i:=0; i<N; i++{
		T[i] = make([]int, N)
		for j:=0; j<N; j++{
			fmt.Scan(&T[i][j])
			if i==0{
				D[i+1][j+1] = T[i][j]
			}
			if j==0{
				D[i+1][j+1] = T[i][j]
			}
		}
	}
	// 二次元累積和（右下に集める）
	for i:=1; i<=N; i++{
		for j:=1; j<=N; j++{
			D[i][j] = D[i-1][j]+D[i][j-1]-D[i-1][j-1]+T[i-1][j-1]
		}
	}
	// あらかじめすべてのとりうる面積についての最大値を計算しておく
	ans := make([]int, N*N+1)
	for i:=0; i<N; i++{
		for ii:=i+1; ii<=N; ii++{
			for j:=0; j<N; j++{
				for jj:=j+1; jj<=N; jj++{
					x := (ii-i)*(jj-j)
					ans[x] = max(ans[x], D[ii][jj]-D[i][jj]-D[ii][j]+D[i][j])
				}
			}
		}
	}
	// これは完全に問題文ミスリードですが与えられるのは「上限」なのでそれ以下でもいいらしい は？？？
	for i := 1; i<=N*N; i++{
		ans[i] = max(ans[i], ans[i-1])
	}
	var Q int
	fmt.Scan(&Q)
	for i:=0; i<Q; i++{
		var q int
		fmt.Scan(&q)
		fmt.Println(ans[q])
	}
}

func min(a, b int) int {
	if a<b{
		return a
	}
	return b
}

func max(a, b int) int {
	if a<b{
		return b
	}
	return a
}