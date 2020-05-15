package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var N int
	fmt.Scan(&N)
	factors := primeFactorization(N)
	keys := []int{}
	for k := range factors {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	ans := []string{}
	for _, k := range keys {
		v := factors[k]
		s := strconv.Itoa(k)
		for v > 0 {
			ans = append(ans, s)
			v--
		}
	}
	fmt.Printf("%d: %s\n", N, strings.Join(ans, " "))
}

func primeFactorization(x int) map[int]int {
	ret := make(map[int]int)
	for i := 2; i*i <= x; i++ {
		for x%i == 0 {
			x /= i
			ret[i]++
		}
	}
	if x > 1 {
		ret[x]++
	}
	return ret
}
