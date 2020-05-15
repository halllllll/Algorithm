// さんすう
// いや〜むずい めっちゃ計算間違えた
package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B, X float64
	fmt.Scan(&A, &B, &X)
	if (A*B)/2 < X/A {
		// こっちむずくない？傾けたときの「空いてる三角」から面積がわかるので X/A + dがA*Bより大きいかどうかで分かる
		l, r := .0, 90.
		for r-l > math.Pow(10, -10) {
			mid := (r + l) / 2
			s := X/A + (math.Pow(A, 2)*math.Tan(mid*math.Pi/180))/2
			if s > A*B {
				r = mid
			} else {
				l = mid
			}
		}
		fmt.Println(l)
	} else {
		// こっちは簡単 横からみて傾けた状態が三角になるのでX/A = (a*d)/2としてdがBより長いかどうかで分かる
		l, r := .0, 90.
		for r-l > math.Pow(10, -10) { // lかrかどっちが満たしてんのかわからんくなったのでどっちでもよくなるようにしただけです
			mid := (l + r) / 2
			d := math.Sqrt(X / A * 2 * math.Tan(mid*math.Pi/180))
			if d > B {
				r = mid
			} else {
				l = mid
			}
		}
		fmt.Println(l)
	}
}
