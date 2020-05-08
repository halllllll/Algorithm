// LISで解けると聞いて無理やり実装したがなんかすげぇ無駄なことをしている気がする
/*
3
3 5
3 7
3 2
4
1 8
5 4
4 3
3 3
0
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var out = bufio.NewWriter(os.Stdout)

type Doll struct {
	H, W int
}

func main() {
	defer out.Flush()
	for {
		var N int
		fmt.Scan(&N)
		if N == 0 {
			break
		}
		var Dolls []Doll
		for i := 0; i < N; i++ {
			var h, r int
			fmt.Scan(&h, &r)
			d := Doll{H: h, W: r}
			Dolls = append(Dolls, d)
		}
		var M int
		fmt.Scan(&M)
		for i := 0; i < M; i++ {
			var h, r int
			fmt.Scan(&h, &r)
			d := Doll{H: h, W: r}
			Dolls = append(Dolls, d)
		}
		sort.Slice(Dolls, func(i, j int) bool {
			if Dolls[i].H < Dolls[j].H {
				return true
			} else if Dolls[i].H == Dolls[j].H {
				if Dolls[i].W < Dolls[j].W {
					return true
				}
			}
			return false
		})
		fmt.Println(Dolls)
		Hs, Ws := make([]int, N+M), make([]int, N+M)
		for i, d := range Dolls {
			Hs[i], Ws[i] = d.H, d.W
		}
		INF := int(10e9)
		DPH, DPW := make([]int, N+M), make([]int, N+M)
		for i := 0; i < N+M; i++ {
			DPH[i], DPW[i] = INF, INF
		}
		DPH[0], DPW[0] = Hs[0], Ws[0]
		length := 1
		for i := 0; i < N+M; i++ {
			if DPH[length-1] < Hs[i] && DPW[length-1] < Ws[i] {
				// 問答無用で追加可能
				DPH[length] = Hs[i]
				DPW[length] = Ws[i]
				length++
			} else if DPH[length-1] == Hs[i] {
				// 更新
				idx := sort.Search(N+M, func(j int) bool { return DPW[j] >= Ws[i] })
				DPW[idx] = Ws[i]
			}
		}
		fmt.Println(DPH)
		fmt.Println(DPW)
		fmt.Fprintln(out, length)
	}
}
