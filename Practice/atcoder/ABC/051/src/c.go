// はい
package main

import (
	"fmt"
	"strings"
)

func main() {
	var Sx, Sy, Tx, Ty int
	fmt.Scan(&Sx, &Sy, &Tx, &Ty)
	ans := ""
	ans += strings.Repeat("R", Tx-Sx) + strings.Repeat("U", Ty-Sy)
	ans += strings.Repeat("L", Tx-Sx) + strings.Repeat("D", Ty-Sy) + "D"
	ans += strings.Repeat("R", Tx-Sx+1) + strings.Repeat("U", Ty-Sy+1) + "LU"
	ans += strings.Repeat("L", Tx-Sx+1) + strings.Repeat("D", Ty-Sy+1) + "R"
	fmt.Println(ans)
}
