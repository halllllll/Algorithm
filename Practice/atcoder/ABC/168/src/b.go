package main

import "fmt"

func main() {
	var K int
	var S string
	fmt.Scan(&K, &S)
	if len(S) <= K {
		fmt.Println(S)
	} else {
		T := ""
		for i, c := range []rune(S) {
			if i < K {
				T += string(c)
			}
		}
		fmt.Println(T + "...")
	}
}
