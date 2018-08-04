package main
import (
	"fmt"
)

func main(){
	var n, x int
	fmt.Scan(&n, &x)
	ms := make([]int, n)
	min :=  999999999999999
	sum := 0
	for i:=0; i<n; i++{
		var mi int
		fmt.Scan(&mi)
		ms[i] = mi
		sum+=mi
		if mi<min{
			min = mi
		}
	}
	fmt.Println(n+(x-sum)/min)
}