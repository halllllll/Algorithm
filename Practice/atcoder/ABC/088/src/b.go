// あえて入力と出力しかいじらない
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush()

	sc.Scan()
	as := sc.Text()
	a, _ := strconv.Atoi(as)
	num := make([]int, a)
	for i := 0; i < a; i++ {
		sc.Scan()
		ns := sc.Text()
		n, _ := strconv.Atoi(ns)
		num[i] = n
	}
	sort.Ints(num)
	// fmt.Printf("a: %d\n", a)
	// fmt.Printf("num: %v\n", num)
	score := 0
	for i := 1; i <= a; i++ {
		if i%2 == 0 {
			// bob's turn
			score -= num[a-i]

		} else {
			// alise's turn
			score += num[a-i]
		}
	}
	fmt.Println(score)
}
