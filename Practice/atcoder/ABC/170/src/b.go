// a + b = x
// 2a+b = y
package main

import "fmt"

func main() {
	var X, Y int
	fmt.Scan(&X, &Y)
	for i := 0; i <= 100; i++ {
		for j := 0; j <= 100; j++ {
			if i+j == X && 2*i+4*j == Y {
				fmt.Println("Yes")
				return
			}
		}
	}
	fmt.Println("No")
}
