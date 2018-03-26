package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!coution!!!! you must use Fprint(out, ) not Print()
	/* --- code ---*/
	nums := make([]int, 3)
	for i := 0; i < 3; i++ {
		sc.Scan()
		t := sc.Text()
		x, _ := strconv.Atoi(t)
		nums[i] = x
	}
	n, a, b := nums[0], nums[1], nums[2]
	ans := 0
	// 10で割っていくやつ
	for i := 1; i <= n; i++ {
		j, c := i, 0
		for 0 < j {
			c += j % 10
			j /= 10
		}
		if a <= c && c <= b {
			ans += i
		}
	}
	fmt.Println(ans)
}
