// 3 6 10 15 21 28 36 45 55 ... はいけるんだなこれが それ以外いけるかどうかは知りませんがヨシ！
// サンプル1をみると、最下段に「それまで出てないやつを集める」、最下段以外の右端に「最下段と共通にしたいやつを加える」をしていく感じだとわかる
// 実装、よくわからんかったので最大値までのテーブルを無理やり作ることにした
// N=1の場合、卑怯じゃないですか？？？？？？？？？？？？？？
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	if N == 1 {
		fmt.Println("Yes")
		fmt.Println(2)
		fmt.Println(1, 1)
		fmt.Println(1, 1)
		return
	}
	ai := 3
	idx := 0
	accept := false
	for ai <= N {
		if ai == N {
			accept = true
		}
		ai = ai + 3 + idx
		idx++
	}
	if !accept {
		fmt.Println("No")
		return
	}
	T := make([][]int, 500) // なんでかはしらん 適当
	for i := 0; i < len(T); i++ {
		T[i] = make([]int, 500)
	}
	// 基礎 手打ちで作成...
	T[0][0], T[1][0] = 1, 1
	T[1][1], T[2][1] = 2, 2
	T[0][1], T[2][0] = 3, 3

	// 構築
	tmp := 4
	hight := 3
	for j := 2; j < 500; j++ {
		for i := 0; i < hight; i++ {
			T[i][j] = tmp
			tmp++
		}
		hight++
	}
	tmp = 4
	width := 3
	for i := 3; i < 500; i++ {
		for j := 0; j < width; j++ {
			T[i][j] = tmp
			tmp++
		}
		width++
	}
	fmt.Println("Yes")
	fmt.Println(idx + 2)
	for i := 0; i <= idx+1; i++ {
		fmt.Printf("%d ", idx+1)
		for j := 0; j <= idx; j++ {
			fmt.Printf("%d ", T[i][j])
		}
		fmt.Println()
	}
}
