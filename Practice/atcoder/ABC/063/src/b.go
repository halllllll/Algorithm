package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	lnh := len([]rune(s))
	t := make(map[string]string, lnh)
	for _, v := range []rune(s) {
		if _, ok := t[string(v)]; !ok {
			t[string(v)] = "うんこ"
		}
	}
	if len(s) == len(t) {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}
}
