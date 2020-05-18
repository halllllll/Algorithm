// まさかAOJ2回目をやることになろうとは（適当にAOJ-ICPCから選んだら過去に解いてた）
package main

import "fmt"

type Pos struct {
	X, Y int
}

func main() {
	for {
		var W, H int
		fmt.Scan(&W, &H)
		if W == 0 || H == 0 {
			return
		}
		steps := []int{-1, 0, 1}
		T := make([][]int, H)
		for i := 0; i < H; i++ {
			T[i] = make([]int, W)
			for j := 0; j < W; j++ {
				var V int
				fmt.Scan(&V)
				T[i][j] = V
			}
		}
		idx := 1
		for i := 0; i < H; i++ {
			for j := 0; j < W; j++ {
				if T[i][j] == 1 {
					cur := Pos{X: j, Y: i}
					T[i][j] += idx
					stack := []Pos{cur}
					for len(stack) > 0 {
						p := stack[len(stack)-1]
						stack = stack[:len(stack)-1]
						// fmt.Println(p, stack)
						for _, a := range steps {
							for _, b := range steps {
								if a == 0 && b == 0 {
									continue
								}
								if 0 <= p.X+b && p.X+b < W && 0 <= p.Y+a && p.Y+a < H {
									if T[p.Y+a][p.X+b] == 1 {
										nexP := Pos{Y: p.Y + a, X: p.X + b}
										stack = append(stack, nexP)
										T[nexP.Y][nexP.X] += idx
									}
								}
							}
						}
					}
					idx++
				}
			}
		}
		fmt.Println(idx - 1)
	}
}
