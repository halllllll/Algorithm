package main

import "fmt"

func main() {
	var N, H, W int
	fmt.Scan(&N, &H, &W)
	fmt.Println((N - (H - 1)) * (N - (W - 1)))
}
