package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main(){
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N, M, K := nextInt(), nextInt(), nextInt()
	A := append([]int{0}, nextInts(N)...)
	B := append([]int{0}, nextInts(M)...)
	for i:=1; i<=N; i++{
		A[i] += A[i-1]
	}
	for i:=1; i<=M; i++{
		B[i] += B[i-1]
	}
	ans := 0
	for i:=0; i<=N; i++{
		rest := K-A[i]
		if rest < 0{
			break
		}
		// golangでupper_boundどうやるんだ？？？？？？・
		/// bidx := max(0, sort.Search(len(B), func(j int)bool{return rest<=B[j]}))
		// bidx := sort.Search(len(B), func(j int)bool{return rest<=B[j]})-1
		// bidx := sort.SearchInts(B, rest)
		// わからんので仕方なく手書き
		left, right := -1, len(B)
		for right - left > 1{
			mid := (left+right)/2
			if rest-B[mid]>=0{
				left = mid
			}else{
				right = mid
			}
		}
		bidx := left
		ans = max(ans, i+bidx)
	}
	fmt.Fprintln(out, ans)
}

func min(a, b int) int {
	if a<b{
		return a
	}
	return b
}

func max(a, b int) int {
	if a<b{
		return b
	}
	return a
}
func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func nextInts(n int) []int{
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
