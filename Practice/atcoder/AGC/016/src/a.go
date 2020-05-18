// アルファベット総当りでやってみる
// アルファベットつーかSに登場する文字
package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	SS := make([]string, len(S))
	target := make(map[string]bool)
	for i, c := range []rune(S) {
		SS[i] = string(c)
		target[string(c)] = true
	}
	keys := []string{}
	for k, _ := range target {
		keys = append(keys, k)
	}
	ans := int(1e8)
	for _, k := range keys {
		tmp_s := append([]string{}, SS...)
		tmp_ans := 0
		for {
			// なんかforで更新しながらのチェックができないのでここで一回やる
			flag := true
			for _, c := range tmp_s {
				if c != k {
					flag = false
				}
			}
			if flag {
				break
			}
			nex_s := []string{}
			for i := 0; i < len(tmp_s)-1; i++ {
				if tmp_s[i] == k || tmp_s[i+1] == k {
					nex_s = append(nex_s, k)
				} else {
					nex_s = append(nex_s, tmp_s[i])
				}
			}
			tmp_ans++
			tmp_s = append([]string{}, nex_s...)
		}
		ans = min(ans, tmp_ans)
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
