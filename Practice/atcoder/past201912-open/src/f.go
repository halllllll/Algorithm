package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	var S string
	fmt.Scan(&S)
	SS := make([]string, len(S))
	for i, c := range []rune(S) {
		SS[i] = string(c)
	}
	ans := []string{}
	r := 1
	for l := 0; l < len(SS); {
		for r < len(SS) && strings.ToUpper(SS[r]) != SS[r] {
			r++
		}
		ans = append(ans, strings.Join(SS[l:r+1], ""))
		l = r + 1
		r = l + 1
	}
	for i := 0; i < len(ans); i++ {
		ans[i] = strings.ToLower(ans[i])
	}
	sort.Strings(ans)
	for i := 0; i < len(ans); i++ {
		a := ans[i]
		aa := make([]string, len(a))
		for j, c := range []rune(a) {
			if j == 0 || j == len(a)-1 {
				aa[j] = strings.ToUpper(string(c))
			} else {
				aa[j] = string(c)
			}
		}
		ans[i] = strings.Join(aa, "")
	}
	fmt.Println(strings.Join(ans, ""))
}
