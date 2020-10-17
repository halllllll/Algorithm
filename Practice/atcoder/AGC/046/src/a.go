package main

import "fmt"

func main() {
	var N float64
	fmt.Scan(&N)
	now := 0.0
	count := 0
	for {
		now += N
		count++
		if now == 360.0 {
			fmt.Println(count)
			return
		}
		if now >= 360.0 {
			now -= 360.0
		}
	}
}
