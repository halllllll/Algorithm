package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var reader = bufio.NewScanner(os.Stdin)

func main() {
	reader.Split(bufio.ScanWords)
	reader.Scan()
	n, _ := strconv.Atoi(reader.Text())
	houses := make([]int, n)
	for i := 0; i < n; i++ {
		reader.Scan()
		a, _ := strconv.Atoi(reader.Text())
		houses[i] = a
	}
	sort.Ints(houses)
	ans := 0
	for i := 1; i < n; i++ {
		ans += houses[i] - houses[i-1]
	}
	fmt.Println(ans)
}
