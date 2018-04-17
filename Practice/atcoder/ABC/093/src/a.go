package main
import (
	"sort"
	"fmt"
	"strings"
)

func main(){
	var s string
	fmt.Scan(&s)
	split := strings.Split(s, "")
	sort.Strings(split)
	if "abc" == strings.Join(split, ""){
		fmt.Println("Yes")
	}else{
		fmt.Println("No")
	}
}