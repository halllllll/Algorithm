package main
import (
	"fmt"
	"math"
)

type floats []float64
func (f floats)find(key float64)bool{
	for _, v := range f{
		if v==key{
			return true
		}
	}
	return false
}

func main(){
	var n int
	fmt.Scan(&n)
	cnt := 0
	// 既出の素数を保存しておく

	for i:=0; i<n; i++{
		var x float64
		var primes floats
		fmt.Scan(&x)
		if !primes.find(x) && check(x){
			cnt++
			primes = append(primes, x)
		}
	}
	fmt.Println(cnt)
}


func check(x float64)bool{
	for i:=2; i<int(math.Sqrt(x))+1; i++{
		if int(x)%i==0{
			return false
		}
	}
	return true
}