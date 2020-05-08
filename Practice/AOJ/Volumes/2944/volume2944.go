package main

import "fmt"

func main() {
	for {
		var N int
		var M float64
		fmt.Scan(&N, &M)
		if N == 0 && M == 0 {
			return
		}
		tmp := 0.0
		for i := 0; i < N; i++ {
			var V float64
			fmt.Scan(&V)
			if M/float64(N) > V {
				tmp += V
			} else {
				tmp += M / float64(N)
			}
		}
		fmt.Println(tmp)
	}
}
