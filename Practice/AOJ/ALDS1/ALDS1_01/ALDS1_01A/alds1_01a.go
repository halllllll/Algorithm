package main
import (
	"fmt"
)

type ints []int
func (is ints)insertionSort(){
	for i:=1; i<len(is); i++{
		v := is[i]
		j := i-1
		for j>=0 && is[j]>v{
			is[j+1]=is[j]
			j--
		}
		is[j+1]=v
		is.printme()
	}
}
func (is ints)printme(){
	for i, v := range is{
		fmt.Print(v)
		if i<len(is)-1{
			fmt.Print(" ")
		}
	}
	fmt.Println()
}

func main(){
	var n int
	fmt.Scan(&n)
	var numbers ints
	for i:=0; i<n; i++{
		var x int
		fmt.Scan(&x)
		numbers = append(numbers, x)
	}
	numbers.printme()
	numbers.insertionSort()
}