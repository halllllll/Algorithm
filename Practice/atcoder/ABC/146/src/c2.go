package main

import "fmt"

func main() {
	var A, B, X int
	fmt.Scan(&A, &B, &X)
	l, r := 0, int(10e8)+1 // なんでだろうね
	for r-l > 0 {
		mid := (r + l) / 2
		d := A*mid + B*keta(mid)
		if X < d {
			r = mid
		} else {
			l = mid + 1
		}
	}
	fmt.Println(l - 1) // なんでだろうね
}

func keta(x int) int {
	ret := 0
	for x > 0 {
		ret += 1
		x /= 10
	}
	return ret
}
