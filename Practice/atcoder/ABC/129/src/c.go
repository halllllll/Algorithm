package main
import "fmt"
func main(){
	var N, M int
	fmt.Scan(&N, &M)
	DP := make([]int, N+101)
	for i:=0; i<M; i++{
		var V int
		fmt.Scan(&V)
		DP[V] = -1
	}
	if DP[1] == 0{
		DP[1]= 1
	}
	if DP[2] == 0{
		if DP[1] > 0{
			DP[2] = 2
		}else{
			DP[2] = 1
		}
	}
	for i:=3; i<=N; i++{
		if DP[i] == -1{
			continue
		}
		if DP[i-2] > 0{
			DP[i] += DP[i-2]
		}
		if DP[i-1] > 0{
			DP[i] += DP[i-1]
		}
		DP[i] %= (int(1e9)+7)
	}
	fmt.Println(DP[N])
}