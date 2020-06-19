// pythonのほうが楽そう
// 文字列ってことで速度が怖いのでテンプレでいくよ

package main
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main(){
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	N := nextInt()
	for i:=0; i<N; i++{
		S := chars(next())
		if len(S) == 2{
			fmt.Fprintln(out, strings.Join(S, ""))
			continue
		}
		ans := []string{S[0]}
		for j:=1; j<len(S)-1; j+=2{
			ans = append(ans, S[j])
		}
		ans = append(ans, S[len(S)-1])
		fmt.Fprintln(out, strings.Join(ans, ""))
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