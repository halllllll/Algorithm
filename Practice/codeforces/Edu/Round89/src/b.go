// 範囲は飛び飛びにならず、ひとつながりで広がっていくので、左右の端で判断する

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
	T := nextInt()
	for i:=0; i<T; i++{
		_, X, M := nextInt(), nextInt(), nextInt()
		left, right := X, X
		for i:=0; i<M; i++{
			L, R := nextInt(),nextInt()
			if L<=left && left<=R{
				left = L
			}
			if L<=right && right <= R{
				right = R
			}
		}
		fmt.Fprintln(out, right - left + 1)
	}
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