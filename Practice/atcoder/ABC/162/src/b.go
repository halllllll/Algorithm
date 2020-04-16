package main
import "fmt"
func main(){
	var N int
	fmt.Scan(&N)
	ans := 0
	for i:=1; i<=N; i++{
		if i % 15 != 0 && i % 3 != 0 && i % 5 != 0{
			ans += i
		}
	}
	fmt.Println(ans)
}