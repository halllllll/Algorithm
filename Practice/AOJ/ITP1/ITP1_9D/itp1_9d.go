package main
import (
	"fmt"
)

func main(){
	var s string
	var n int
	fmt.Scan(&s, &n)
	for i:=0; i<n; i++{
		var op string
		var a, b int
		fmt.Scan(&op, &a, &b)
		switch op{
		case "print":
			fmt.Println(s[a:b+1])
		case "reverse":
			s = Reverse(s, a, b)
			// fmt.Printf("reversed: %s\n", s)
		case "replace":
			var p string
			fmt.Scan(&p)
			s = s[:a]+p+s[b+1:]
			// fmt.Printf("replased: %s\n", s)
		}
	}
}


func Reverse(s string, a int, b int) string {
	r := []rune(s)
	for i, j := a, b; i < (a+b)/2+1; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}