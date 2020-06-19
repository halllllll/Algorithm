package main
import "fmt"
func main(){
	var N int
	fmt.Scan(&N)
	ans := make([]int, N)
	for i:=0; i<N; i++{
		var A, B int
		fmt.Scan(&A, &B)
		ans[i] = min(A, min(B, (A+B)/3))
	}
	for _, a := range ans{
		fmt.Println(a)
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