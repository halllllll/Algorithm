// 全探索してみます それぞれが「おともだち国会である/でない」の2つの状態なのでbitでよさそうです
package main

import "fmt"

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	T := make([][]bool, N)
	for i := 0; i < N; i++ {
		T[i] = make([]bool, N)
	}
	for i := 0; i < M; i++ {
		var X, Y int
		fmt.Scan(&X, &Y)
		X--
		Y--
		T[Y][X] = true
		T[X][Y] = true
	}
	ans := 0
	for bit := 0; bit < (1 << uint(N)); bit++ {
		tmp := []int{}
		for i := 0; i < N; i++ {
			if (bit>>uint(i))&1 == 1 {
				// 「ここでビット立ってるやつを一旦グループとみなす」をして、
				// 「グループ同士でおともだちかどうかをあとで二重ループなりDFSなりで判断」する
				tmp = append(tmp, i)
			}
		}
		flag := true
		for i := 0; i < len(tmp); i++ {
			for j := i + 1; j < len(tmp); j++ {
				if !T[tmp[i]][tmp[j]] { // つまりせっかく用意したテーブルは右上半分の三角行列だけでいいわけです（この問題においては）
					flag = false
				}
			}
		}
		if flag {
			ans = max(ans, len(tmp))
		}
	}
	fmt.Println(ans)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
