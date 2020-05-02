package main
import "fmt"
func main(){
	var S string
	fmt.Scan(&S)
	ans := 0
	for _, c := range []rune(S){
		s := string(c)
		if s== "+"{
			ans+=1
		}else{
			ans-=1
		}
	}
	fmt.Println(ans)
}