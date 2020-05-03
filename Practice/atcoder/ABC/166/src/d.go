// これ気づかんかった、もっと冷静になるべきだった
// Xの上限が10^9なのだがこれがヒント
//
// ...らしいんだけど、だからなんでここにたどり着けるのか一切わからん

package main

import (
	"fmt"
	"math"
)

func main() {
	var X int
	fmt.Scan(&X)
	for i := -300; i <= 300; i++ {
		for j := -300; j <= 300; j++ {
			if math.Pow(float64(i), float64(5))-math.Pow(float64(j), float64(5)) == float64(X) {
				fmt.Println(i, j)
				return
			}
		}
	}
}
