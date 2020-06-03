package main

import "fmt"

func main() {
	var A, B int
	fmt.Scan(&A, &B)
	rec := func(i, smaller, include4or9 int, target []int) int {
		if i == len(target) {
			if include4or9 == 1 {
				return 0
			} else {
				return 1
			}
		}
		ret := 0
		upper := 10
		if smaller == 0 {
			upper = target[i] + 1
		}
		for j := 0; j < upper; j++ {
			nex_smaller := 1
			if j >= target[i] || smaller == 1 {

			}
		}
		return ret
	}
}
