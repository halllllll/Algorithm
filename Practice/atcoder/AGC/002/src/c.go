// 隣り合うのをL以上になるようにくっつけていきたいね 一箇所でもみつければあとは隣接してるのをくっつけていきたいね
// -> てんでダメでした
// よくよくみたらおかしいところ 端から切り離す感じにするようにした
// -> なぜかWA
// 3つ並んでる総和がL未満なら見込み0ってことか
// -> そういうことではない
// 両端から切り離す"がちゃんとできてなかったバグだった

package main

import "fmt"

func main() {
	var N, L int
	fmt.Scan(&N, &L)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}

	idx := -1
	for i := 1; i < N; i++ {
		if A[i-1]+A[i] >= L {
			idx = i
			break
		}
	}

	if idx == -1 {
		fmt.Println("Impossible")
		return
	}
	P := []int{}
	for i := N - 1; i > idx; i-- {
		P = append(P, i)
	}
	for i := 1; i < idx; i++ {
		P = append(P, i)
	}
	P = append(P, idx)
	fmt.Println("Possible")
	for _, p := range P {
		fmt.Println(p)
	}
}

// 10 4
// 2 1 1 4 2 3 1 2 1 2

// 5 3
// 1 1 3 1 1

// 5 5
// 1 1 3 2 1
