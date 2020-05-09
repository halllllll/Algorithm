package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	T := make([]string, N)
	// 基準が欲しいので
	fmt.Println(0)
	var Z string
	fmt.Scan(&Z)
	if Z == "Vacant" {
		return
	}
	T[0] = Z
	l, r := 0, N
	for {
		if r-l == 0 {
			l, r = 0, N/2
		}
		mid := (l + r) / 2
		fmt.Println(mid)
		var A string
		fmt.Scan(&A)
		if A == "Vacant" {
			return
		} 
		if A == T[mid] {
			r = mid
		} else {
			l = mid + 1
		}
	}
}
