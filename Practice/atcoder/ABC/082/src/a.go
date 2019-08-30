package main

import "fmt"

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	// なんの挙動も確認してないけどこんな適当でいいのかな
	fmt.Println((a + b + 1) / 2)
}
