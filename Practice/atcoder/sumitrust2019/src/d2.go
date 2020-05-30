// 全探索やね
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	var S string
	fmt.Scan(&S)
	SS := make([]string, N)
	for i, c := range []rune(S) {
		SS[i] = string(c)
	}
	ans := 0
	for i := 0; i < 1000; i++ {
		tmp := 0
		ss := stringfy(i)
		for _, sv := range SS {
			if ss[tmp] == sv {
				tmp++
			}
			if tmp == 3 {
				ans++
				break
			}
		}
	}
	fmt.Println(ans)
}

func stringfy(x int) []string {
	ss := fmt.Sprintf("%03d", x)
	ret := make([]string, len(ss))
	for i, c := range []rune(ss) {
		ret[i] = string(c)
	}
	return ret
}
