// 横幅で昇順ソートすると、「同じ横幅の場合、縦幅は小さい方がいい」となる。
// なので横幅でソートしたあと、縦幅はLISを使える
// 「縦幅の比較は降順ソートにする」 <- ???????????????????????????????????????
// てっきり[H][W]二次元使うかと思ったら↑より、Wだけにするのね...
// 応用が一切できない 死
// atcoderの過去問の言語バージョンが未だに古いままなので仕方なく19089475893年前の実装でやってやる

package main

import (
	"fmt"
	"sort"
)

type Present struct {
	H, W int
}

type ByAndMoreHnMoreW []Present

func (p ByAndMoreHnMoreW) Len() int {
	return len(p)
}
func (p ByAndMoreHnMoreW) Less(i, j int) bool {
	if p[i].H < p[j].H {
		return true
	} else if p[i].H == p[j].H && p[i].W > p[j].W {
		return true
	} else {
		return false
	}
}
func (p ByAndMoreHnMoreW) Swap(i, j int) {
	p[i], p[j] = p[j], p[i]
}

func main() {
	var N int
	fmt.Scan(&N)
	Prezents := make([]Present, N)
	for i := 0; i < N; i++ {
		var h, w int
		fmt.Scan(&h, &w)
		Prezents[i] = Present{H: h, W: w}
	}
	sort.Sort(ByAndMoreHnMoreW(Prezents))
	// ここから
	AnsPrezents := make([]int, N)
	for i := 0; i < N; i++ {
		AnsPrezents[i] = Prezents[i].W
	}
	// ここまで
	// あとは普通のLIS
	INF := int(10e15)
	L := make([]int, N)
	for i := 0; i < N; i++ {
		L[i] = INF
	}
	length := 1
	L[0] = AnsPrezents[0]
	for i := 0; i < N; i++ {
		if L[length-1] < AnsPrezents[i] {
			L[length] = AnsPrezents[i]
			length++
		} else {
			idx := sort.Search(N, func(j int) bool {
				return L[j] >= AnsPrezents[i]
			})
			L[idx] = AnsPrezents[i]
		}
	}
	fmt.Println(length)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
