package main
import (
	"fmt"
)

var roman = []int{1000, 500, 100, 50, 10, 5, 1}
var romachar = []string{"M", "D", "C", "L", "X", "V", "I"}

func main(){
	/*
	ans := 0
	for i:=1; i<=3999; i++{
		cnt, t := 0 , i
		for _, v := range roman{
			appear:= 1
			for 0<t/v && appear<4{
				appear++
				t-=v
				cnt++
			}
		}
		if cnt==12{
			fmt.Printf("find! %d\n", i)
			romaned(i)
			ans++
		}
	}
	fmt.Println(ans)
	*/
	romaned(290)
}

func romaned(n int){
	for idx, r := range roman{
		for 0<n/r{
			fmt.Print(romachar[idx])
			n-=r
		}
	}
	fmt.Println()
}