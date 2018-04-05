package main
import "fmt"

func main(){
	var x, y int
	fmt.Scan(&x, &y)
	ans := gcd(x, y)
	fmt.Println(ans)
}

func gcd(x, y int)(ret int){
	if x<y{
		gcd(y, x)
	}
	for 0<y{
		x, y = y, x%y
	}
	return x
}