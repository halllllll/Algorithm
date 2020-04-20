package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	T := make(map[string]string)
	A := make(map[string]string)
	for i := 0; i < 10; i++ {
		var V string
		fmt.Scan(&V)
		si := strconv.Itoa(i)
		T[V] = si
	}
	var N int
	fmt.Scan(&N)
	INPUT := []int{}
	for i := 0; i < N; i++ {
		var a string
		fmt.Scan(&a)
		tmp := ""
		for _, c := range []rune(a) {
			tmp += T[string(c)]
		}
		A[a] = tmp
		ti, _ := strconv.Atoi(tmp)
		INPUT = append(INPUT, ti)
	}
	// fmt.Println(A)
	A_versa := make(map[string]string)
	for k, v := range A {
		A_versa[v] = k
	}
	sort.Ints(INPUT)
	// fmt.Printf("input1 = %v\n", INPUT)
	// fmt.Println(A_versa)
	for _, a := range INPUT {
		as := strconv.Itoa(a)
		fmt.Println(A_versa[as])
	}
}
