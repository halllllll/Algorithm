package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		var v int
		fmt.Scan(&v)
		if v == 0 {
			fmt.Println(i + 1)
			return
		}
	}
}
