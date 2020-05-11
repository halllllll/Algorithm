// 素因数分解して冪数/Nをかけていくのでどうだ
// サンプル4がありがたい

package main

import "fmt"

func main() {
	var N, P int
	fmt.Scan(&N, &P)
	dividers := make(map[int]int)
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

	ans := 1
	for k, v := range dividers {
		if v/N > 0 {
			ans *= pow(k, v/N)
		}
	}
	fmt.Println(ans)
}

func pow(a, b int) (ret int) {
	ret = a
	for i := 0; i < b-1; i++ {
		ret *= a
	}
	return
}
