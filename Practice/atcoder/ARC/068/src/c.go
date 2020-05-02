// よるかつからきました

package main

import "fmt"

func main() {
	// 6,5,6,5...を頑張って繰り返す
	// 6までは1回 11までは2回 17までは3回 22までは4回 27までは5回 33までは6回...
	// 38(5) 44(6) 49(7) 55(8) 60(9) 66(11) 71(12) 77(13)

	var X int
	fmt.Scan(&X)
	if X%11 == 0 {
		fmt.Println(X / 11 * 2)
	} else {
		if X%11 <= 6 {
			fmt.Println(X/11*2 + 1)
		} else {
			fmt.Println(X/11*2 + 2)
		}
	}
}
