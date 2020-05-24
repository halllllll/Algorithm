package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	fmt.Println(int(1<<uint64(M)) * (1900*M + (N-M)*100))
}
