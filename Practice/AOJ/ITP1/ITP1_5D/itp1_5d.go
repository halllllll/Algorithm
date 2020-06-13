// なんか落ち着いて見ればgotoもwhileでいけるんだな
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var N int
	fmt.Scan(&N)
	i := 1
	ans := []string{""}
	for i <= N {
		x := i
		if x%3 == 0 {
			ans = append(ans, strconv.Itoa(i))
		} else {
			for x > 0 {
				if x%10 == 3 {
					ans = append(ans, strconv.Itoa(i))
					break
				}
				x /= 10
			}
		}
		i++
	}
	fmt.Println(strings.Join(ans, " "))
}
