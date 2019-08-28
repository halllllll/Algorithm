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
	defer out.Flush()
	sc.Scan()
	ns := sc.Text()
	n, _ := strconv.Atoi(ns)
	sc.Scan()
	ys := sc.Text()
	y, _ := strconv.Atoi(ys)
	// 10000a+5000b+1000c = y, a+b+c=n
	fin := false
	for a := 0; a <= n && fin == false; a++ {
		for b := 0; b <= n; b++ {
			c := n - a - b
			if 0 <= c && a*10000+b*5000+c*1000 == y {
				fmt.Fprintf(out, "%d %d %d\n", a, b, c)
				fin = true
				break
			}
		}
	}
	if fin == false {
		fmt.Fprintln(out, "-1 -1 -1")
	}
}
