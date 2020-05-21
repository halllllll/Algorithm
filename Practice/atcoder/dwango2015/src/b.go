// runeでそのまんまやった
// 公差1初項1の等差数列の和 = n(n+1)/2
package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scan(&S)
	idx, ans, tmp := 0, 0, 0
	for idx < len(S)-1 {
		if S[idx] == 50 && S[idx+1] == 53 {
			idx += 2
			tmp++
		} else {
			idx++
			if tmp > 0 {
				ans += tmp * (tmp + 1) / 2
			}
			tmp = 0
		}
	}
	if tmp > 0 {
		ans += tmp * (tmp + 1) / 2
	}
	fmt.Println(ans)
}
