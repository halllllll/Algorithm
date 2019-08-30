package main

import (
	"bytes"
	"fmt"
)

// bytesのhassuffixを使う

var texts = [][]byte{[]byte("dream"), []byte("dreamer"), []byte("erase"), []byte("eraser")}

func main() {
	var s []byte
	fmt.Scan(&s)
	ans := false
	for {
		// sがtextを末尾に持つかどうか
		have := false
		for _, t := range texts {
			// もっていたらそれを消す
			if bytes.HasSuffix(s, t) {
				s = s[:len(s)-len(t)]
				have = true
				break
			}
		}
		if have {
			continue
		} else if len(s) == 0 {
			ans = true
			break
		} else {
			break
		}
	}
	if ans {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
