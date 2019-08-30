package main

import (
	"fmt"
)

func main() {
	var w, h, n int
	fmt.Scan(&w, &h, &n)
	ichi := make([]int, w)
	for i := 0; i < w; i++ {
		ichi[i] = 1
	}
	zero := make([]int, w)
	for i := 0; i < w; i++ {
		zero[i] = 0
	}
	m := make([][]int, h)
	for y := 0; y < h; y++ {
		m[y] = make([]int, w)
		copy(m[y], ichi)
	}

	// ここからmを書き換えていく
	for k := 0; k < n; k++ {
		var x, y, t int
		fmt.Scan(&x, &y, &t)
		// 全部やってるとW*H*Nで10000000で間に合うんだけどダルいのでちょと省く
		switch t {
		case 1:
			// 0<j<xまで潰す
			for i := 0; i < h; i++ {
				for j := 0; j < x; j++ {
					m[i][j] = 0
				}
			}
		case 2:
			// x<=j<wまで潰す
			for i := 0; i < h; i++ {
				for j := x; j < w; j++ {
					m[i][j] = 0
				}
			}
		case 3:
			// 0<=i<yまで潰す
			for i := 0; i < y; i++ {
				copy(m[i], zero)
			}
		case 4:
			// y<=i<hまで潰す
			for i := y; i < h; i++ {
				copy(m[i], zero)
			}
		}

		// テスト
		/*
			fmt.Println("-----------")
			for y := 0; y < h; y++ {
				fmt.Println(m[y])
			}
		*/
	}

	// 最後に残った1を計算しておわり
	ans := 0
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			ans += m[y][x]
		}
	}
	fmt.Println(ans)
}
