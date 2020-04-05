package main
import "fmt"
func main(){
	ans := 42
	for ans < 130000000{
		ans *= 2
	}
	fmt.Println(ans)
}