package main
import (
	"fmt"
	"strings"
)

func main(){
	var s, p string
	fmt.Scan(&s, &p)
	s = s+s[:len(p)]
	ans := strings.Index(s, p)
	if ans==-1{
		fmt.Println("No")
	}else{
		fmt.Println("Yes")
	}
}