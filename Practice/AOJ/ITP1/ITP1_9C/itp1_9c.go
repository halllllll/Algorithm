package main
import (
	"fmt"
)
func main(){
	var n int
	fmt.Scan(&n)
	var ap, bp int
	for i:=0; i<n; i++{
		var a, b string
		fmt.Scan(&a, &b)
		if a>b{
			ap+=3
		}else if a<b{
			bp+=3
		}else{
			ap+=1
			bp+=1
		}
	}
	fmt.Println(ap, bp)
}