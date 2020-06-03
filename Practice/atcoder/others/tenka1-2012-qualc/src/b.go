// 入力めんどくせ 一枚ずつにしてから4パターンそれぞれ探索 捨てる動作は最後にまとめてやればいい
// ただの作業 某aizaみたい
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	var S string
	fmt.Scan(&S)
	T := []string{}
	idx := 0
	for idx < len(S) {
		suite := string([]rune(S)[idx])
		idx++
		if unicode.IsNumber([]rune(S)[idx]) && string([]rune(S)[idx]) == "1" {
			T = append(T, suite+"10")
			idx += 2
		} else {
			T = append(T, suite+string([]rune(S)[idx]))
			idx++
		}
	}
	ss, hs, ds, cs := make(map[string]bool), make(map[string]bool), make(map[string]bool), make(map[string]bool)
	stack := []string{}
	for _, t := range T {
		if t == "S10" || t == "SJ" || t == "SQ" || t == "SK" || t == "SA" {
			ss[t] = true
		}
		if t == "H10" || t == "HJ" || t == "HQ" || t == "HK" || t == "HA" {
			hs[t] = true
		}
		if t == "D10" || t == "DJ" || t == "DQ" || t == "DK" || t == "DA" {
			ds[t] = true
		}
		if t == "C10" || t == "CJ" || t == "CQ" || t == "CK" || t == "CA" {
			cs[t] = true
		}
		if len(ss) == 5 || len(hs) == 5 || len(ds) == 5 || len(cs) == 5 {
			break
		}
		stack = append(stack, t)
	}
	ans := []string{}
	if len(ss) == 5 {
		for _, s := range stack {
			if _, ok := ss[s]; !ok {
				ans = append(ans, s)
			}
		}
	} else if len(hs) == 5 {
		for _, s := range stack {
			if _, ok := hs[s]; !ok {
				ans = append(ans, s)
			}
		}
	} else if len(ds) == 5 {
		for _, s := range stack {
			if _, ok := ds[s]; !ok {
				ans = append(ans, s)
			}
		}
	} else if len(cs) == 5 {
		for _, s := range stack {
			if _, ok := cs[s]; !ok {
				ans = append(ans, s)
			}
		}
	} else {
		panic("fuck")
	}
	if len(ans) == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(strings.Join(ans, ""))
	}
}
