package main
import (
	"fmt"
	"math"
)

func main(){
	var a, b, angle float64
	fmt.Scan(&a, &b, &angle)


	s :=.5*a*b*math.Sin(math.Pi/180.0*angle)
	fmt.Println(s)
	// 余弦定理
	c := math.Pow(a, 2.0)+math.Pow(b, 2.0)-2.0*a*b*math.Cos(math.Pi/180.0*angle)
	c = math.Sqrt(c)
	fmt.Println(a+b+c)
	// S=1/2(bottoh*hight)
	h := 2.0*s/a
	fmt.Println(h)

}