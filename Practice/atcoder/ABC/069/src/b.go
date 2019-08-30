package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	fmt.Printf("%v%v%v\n", string(s[0]), len(s)-2, string(s[len(s)-1]))
}
