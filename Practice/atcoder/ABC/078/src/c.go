// 期待値とかしらねぇけどサンプル2を眺めて分解してそれをもとにサンプル3を再構築したら見えてきた
package main

import "fmt"

var n, m int

func main() {
	fmt.Scan(&n, &m)
	b := 1
	for i := 0; i < m; i++ {
		b *= 2
	}
	fmt.Println(((n-m)*100 + 1900*m) * b)
}
