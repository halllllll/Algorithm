package main
import (
	"fmt"
)

func main(){
	var n int
	fmt.Scan(&n)
	s := make([]int, n)
	for i:=0; i<n; i++{
		var x int 
		fmt.Scan(&x)
		s[i] = x
	}
	var q int
	fmt.Scan(&q)
	t := make([]int, q)
	for i:=0; i<q; i++{
		var x int
		fmt.Scan(&x)
		t[i] = x
	}
	ans := 0
	for _, x := range t{
		for _, y := range s{
			if x==y{
				ans++
				break
			}
		}
	}
	fmt.Println(ans)
}