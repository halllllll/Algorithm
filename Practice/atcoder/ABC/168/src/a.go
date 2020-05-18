package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	N %= 10
	if N == 2 || N == 4 || N == 5 || N == 7 || N == 9 {
		fmt.Println("hon")
	} else if N == 3 {
		fmt.Println("bon")
	} else {
		fmt.Println("pon")
	}
}
