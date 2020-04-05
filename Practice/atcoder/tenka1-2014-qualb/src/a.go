// 登場する場所のインデックスを保存して置き換える
package main

import "fmt"

func main() {
	var s string
	hagiya := "HAGIYA"
	hagizile := "HAGIXILE"
	fmt.Scan(&s)
	idx := -1
	for i := 0; i < len([]rune(s))-5; i++ {
		flag := true
		// fmt.Printf("now s[i] = %s\n", string([]rune(s)[i]))
		for j := 0; j < 6; j++ {

			if string([]rune(s)[i+j]) != string([]rune(hagiya)[j]) {
				flag = false
			}
		}
		if flag {
			idx = i
			break
		}
	}
	if idx == -1 {
		fmt.Println("え？？？？")
		return
	}
	pre, epi := "", ""
	for i := 0; i < idx; i++ {
		pre += string([]rune(s)[i])
	}
	for i := idx + 6; i < len([]rune(s)); i++ {
		epi += string([]rune(s)[i])
	}
	fmt.Println(pre + hagizile + epi)
}
