// 適当に探索？ 最初のやつをSとして決め打ちして矛盾なければそれ、駄目だったらWでやってみて矛盾なければそれ、どっちも駄目ならお前はもう駄目だ 駄目
// 構築ってなんだ？
// 最後まで調べないとわからない系？
package main

import (
	"fmt"
	"strings"
)

func main() {
	var N int
	fmt.Scan(&N)
	var S string
	fmt.Scan(&S)
	tmp1, tmp2, tmp3, tmp4 := make([]string, N), make([]string, N), make([]string, N), make([]string, N)
	tmp1[0], tmp1[1] = "S", "S"
	tmp2[0], tmp2[1] = "S", "W"
	tmp3[0], tmp3[1] = "W", "W"
	tmp4[0], tmp4[1] = "W", "S"
	base := make([]string, N)
	for i, v := range []rune(S) {
		base[i] = string(v)
	}
	if ok, ret := program(base, tmp1); ok {
		fmt.Println(strings.Join(ret, ""))
	} else if ok, ret := program(base, tmp2); ok {
		fmt.Println(strings.Join(ret, ""))
	} else if ok, ret := program(base, tmp3); ok {
		fmt.Println(strings.Join(ret, ""))
	} else if ok, ret := program(base, tmp4); ok {
		fmt.Println(strings.Join(ret, ""))
	} else {
		fmt.Println(-1)
	}
}

func program(base []string, arr []string) (ok bool, ret []string) {
	for i := 1; i < len(arr)-1; i++ {
		s := base[i]
		if s == "o" {
			if arr[i] == "S" {
				arr[i+1] = arr[i-1]
			} else {
				if arr[i-1] == "S" {
					arr[i+1] = "W"
				} else {
					arr[i+1] = "S"
				}
			}
		} else {
			if arr[i] == "S" {
				if arr[i-1] == "S" {
					arr[i+1] = "W"
				} else {
					arr[i+1] = "S"
				}
			} else {
				arr[i+1] = arr[i-1]
			}
		}
	}
	flag := true
	if base[0] == "o" {
		if arr[0] == "S" {
			if arr[len(arr)-1] != arr[1] {
				flag = false
			}
		} else {
			if arr[len(arr)-1] == arr[1] {
				flag = false
			}
		}
	} else {
		if arr[0] == "S" {
			if arr[len(arr)-1] == arr[1] {
				flag = false
			}
		} else {
			if arr[len(arr)-1] != arr[1] {
				flag = false
			}
		}
	}
	if base[len(arr)-1] == "o" {
		if arr[len(arr)-1] == "S" {
			if arr[len(arr)-2] != arr[0] {
				flag = false
			}
		} else {
			if arr[len(arr)-2] == arr[0] {
				flag = false
			}
		}
	} else {
		if arr[len(arr)-1] == "S" {
			if arr[len(arr)-2] == arr[0] {
				flag = false
			}
		} else {
			if arr[len(arr)-2] != arr[0] {
				flag = false
			}
		}
	}
	return flag, arr
}
