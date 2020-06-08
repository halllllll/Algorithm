// 雑 推敲してない
package main

import "fmt"

func main() {
	var X, A, B int
	fmt.Scan(&X, &A, &B)
	if A-B >= 0 {
		fmt.Println("delicious")
	} else if X >= B-A {
		fmt.Println("safe")
	} else {
		fmt.Println("dangerous")
	}
}
