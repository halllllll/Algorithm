package main

import "fmt"

var s string
var w int

func main() {
	fmt.Scan(&s, &w)
	ans := []string{}
	for i := 0; i < len([]rune(s)); i += w {
		ans = append(ans, string([]rune(s)[i]))
	}
	for _, a := range ans {
		fmt.Print(a)
	}
	fmt.Println()
}
