package main

import (
	"fmt"
)

func ten2kisu(n int, base int) (ret int) {
	// 10進数からn進数に変換
	// こいつにセットしていく
	set := make([]int, 0)
	/*
		えっと なんだっけ 基数変換
		たとえば6を2進数に直すとき
		6を2で割った余りが0 商が3
		3を2で割った余りが1 商が1
		1を2で割った余りが1 商が0
		余りを逆順にして110、というやつ
	*/
	for {
		set = append(set, n%base)
		n /= base
		if n == 0 {
			break
		}
	}
	// 逆順にっつってもgoのスライスはなんか余計な増え方するんだよな
	for i := len(set) - 1; i >= 0; i-- {
		x := 1
		for j := 0; j < i; j++ {
			x *= 10
		}
		ret += set[i] * x
	}
	return
}

func naru(n int) (ret int) {
	// 入ってきたやつの各桁を桁数を乗じて足す
	// ret := 0
	// まず何桁あるか数える
	keta := 1
	temp1, temp2 := n, n
	for {
		if temp1/10 == 0 {
			break
		}
		keta += 1
		temp1 /= 10
	}
	// fmt.Printf("%dの桁数: %d\n", n, keta)
	// 次に小さい桁から順にとって足していく べつに小さい順じゃなくていいけど10で割った余りで出せるので
	for {
		x := temp2 % 10
		// fmt.Printf("ターゲットとなる値: %d\n", x)
		for i := 1; i < keta; i++ {
			x *= temp2 % 10
		}
		// fmt.Printf("それを%d乗した: %d\n", keta, x)
		ret += x
		if temp2/10 == 0 {
			break
		}
		temp2 /= 10
	}
	return
}

func main() {
	ans := make([]int, 0)
	for i := 11; len(ans) < 8; i++ {
		// 8進数に変換
		oct := ten2kisu(i, 8)
		if oct == ten2kisu(naru(oct), 8) {
			ans = append(ans, oct)
		}
	}
	fmt.Println(ans)
}
