// 3500なのに872 1012974 1539173474040とはいかに...と思ったが「保証されている」ってだけだった
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	for h := 1; h <= 3500; h++ {
		for n := 1; n <= 3500; n++ {
			if 4*n*h > N*h+N*n && N*h*n%(4*n*h-N*h-N*n) == 0 {
				w := N * h * n / (4*n*h - N*h - N*n)
				if w > 0 {
					fmt.Println(h, n, w)
					return
				}
			}
		}
	}
}
