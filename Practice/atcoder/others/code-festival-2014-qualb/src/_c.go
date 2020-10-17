package main

import "fmt"

func main() {
	var S1, S2, S3 string
	fmt.Scan(&S1, &S2, &S3)
	T1, T2, T3 := make(map[string]int), make(map[string]int), make(map[string]int)
	for _, c := range []rune(S1) {
		T1[string(c)]++
	}
	for _, c := range []rune(S2) {
		T2[string(c)]++
	}
	for _, c := range []rune(S3) {
		T3[string(c)]++
	}
	AN, BN = len(S1), len(S1)
	for k, v := range T3 {
		tmp := 0
		if _, ok := T1[k]; ok {
			AN -= T1[k]
			tmp += T1[k]
		}
		if _, ok := T2[k]; ok {
			BN -= T2[k]
			tmp += T2[k]
		}
		if tmp < v {
			fmt.Println("NO")
			return
		}
		// 取りすぎたぶんを還元
		if AN < 0 && BN < 0 {
			
		} else if AN < 0 {

		} else if BN < 0 {

		}
	}
	fmt.Println("YES")
}
