package main
import (
	"fmt"
)

const N = 100

func main(){
	cnt := 0
	for i:=0; i<=N; i++{
		for j:=0; j<=N-i; j++{
			for k:=0; k<=N-(i+j); k++{
				if i+j+k==N && ((i>j && i>k ) || (j>i && j>k) || (k>i && k>j)){
					cnt++
					// fmt.Printf("i,j,k=[%d, %d, %d]\n", i, j, k)
				}
			}
		}
	}
	fmt.Println(cnt)
}
