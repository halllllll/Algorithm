package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	// sの末尾から一致する単語を消していく
	ans := false
	for {
		var tmp = s
		l := len(tmp)
		switch {
		case 0 == l:
			ans = true
			break
		case 6 < l:
			if tmp[len(tmp)-7:] == "dreamer" {
				tmp = tmp[:len(tmp)-7]
				s = tmp
				continue
			}
			fallthrough
		case 5 < l:
			if tmp[len(tmp)-6:] == "eraser" {
				tmp = tmp[:len(tmp)-6]
				s = tmp
				continue
			}
			fallthrough
		case 4 < l:
			if tmp[len(tmp)-5:] == "dream" || tmp[len(tmp)-5:] == "erase" {
				tmp = tmp[:len(tmp)-5]
				s = tmp
				continue
			}
			fallthrough
		default:
			break
		}
		if tmp == s {
			break
		}
	}
	if ans {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
