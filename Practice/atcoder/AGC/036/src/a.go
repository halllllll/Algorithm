// Cを原点として, 素因数分解して順番にAxとByに割り当てる感じでいけそうな気がする
// -> 試しにサンプル3を分解したら駄目そうでした

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	dividers := make(map[int]int)
	P := N
	for i := 2; i*i <= P; i++ {
		tmp := 0
		_P := P
		_pow := i
		for _P%i == 0 {
			_pow *= i
			tmp++
			_P /= i
		}
		if tmp > 0 {
			dividers[i] = tmp
			P /= (_pow / i)
		}
	}
	if P > 0 {
		dividers[P] = 1
	}
	fmt.Println(dividers)
}
