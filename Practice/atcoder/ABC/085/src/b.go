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
	// map使う
	sc.Scan()
	ns := sc.Text()
	n, _ := strconv.Atoi(ns)
	dict := make(map[int]bool)
	for i := 0; i < n; i++ {
		sc.Scan()
		as := sc.Text()
		a, _ := strconv.Atoi(as)
		// せっかくなのでgo的な文法を使う
		if _, ok := dict[a]; ok == false {
			dict[a] = true
		}
	}
	fmt.Println(len(dict))
}
