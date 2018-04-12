package main
import (
	"fmt"
	"math"
)

func main(){
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i:=0; i<n; i++{
		var _a int
		fmt.Scan(&_a)
		a[i] = _a
	}
	b := make([]int, n)
	for i:=0; i<n; i++{
		var _b int
		fmt.Scan(&_b)
		b[i] = _b
	}
	for i:=1; i<=4; i++{
		mincofusukii(a, b, i)
	}
}

func mincofusukii(a []int, b []int, c int){
	var ans float64
	if c<4{
		for i:=0; i<len(a); i++{
			ans+=math.Pow(math.Abs(float64(a[i])-float64(b[i])), float64(c))
		}
		ans = math.Pow(ans, 1.0/float64(c))
	}else{
		for i:=0; i<len(a); i++{
			ans = math.Max(ans, math.Abs(float64(a[i])-float64(b[i])))
		}
	}
	fmt.Println(ans)
}