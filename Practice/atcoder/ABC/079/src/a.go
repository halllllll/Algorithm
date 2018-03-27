package main

import "fmt"

func main() {
	// 下3桁の場合 下三桁だけとったら111で割り切れる
	// 上3桁の場合 上三桁だけとったら同上
	var n int
	fmt.Scan(&n)
	simo := (n - (n / 1000)) % 111
	kami := (n / 10) % 111
	if simo == 0 || kami == 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
