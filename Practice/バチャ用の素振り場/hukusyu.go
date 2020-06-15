// Biに対してAi,CiにLowerBound, UpperBound

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
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N := nextInt()
	A, B, C := nextInts(N), nextInts(N), nextInts(N)
	// sort.Sort(sort.Reverse(sort.IntSlice(A)))
	sort.Ints(A)
	sort.Ints(B)
	// sort.Ints(C)
	sort.Sort(sort.Reverse(sort.IntSlice(C)))
	fmt.Println(A)
	fmt.Println(B)
	fmt.Println(C)

	ans := 0
	for i := 0; i < N; i++ {
		smaller := sort.Search(N, func(j int) bool {
			return B[i] < A[i]
		})
		larger := sort.Search(N, func(j int) bool {
			return C[j] < B[i]
		})
		fmt.Printf("B[i] = %d, smaller = %d, larget = %d\n", B[i], smaller, larger)
		if smaller != N && larger != N && A[smaller] < B[i] && B[i] < C[larger] {
			// ans += (N - (smaller + 1))*()
		}
	}
	fmt.Fprintln(out, ans)
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}

func nextStrings(n int) []string {
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		ret[i] = next()
	}
	return ret
}

func chars(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
	}
	return ret
}
