package main

import "fmt"

func main() {
	var A, B int
	fmt.Scan(&A, &B)
	adivs, bdivs := enumPrime(A), enumPrime(B)
	ans := 0
	for ak, _ := range adivs {
		if _, ok := bdivs[ak]; ok {
			ans++
		}
	}
	fmt.Println(ans)
}

func enumPrime(P int) (dividers map[int]int) {
	dividers = make(map[int]int)
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
	dividers[1] = 1
	return
}
