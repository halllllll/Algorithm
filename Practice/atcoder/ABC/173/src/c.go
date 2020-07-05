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
	H, W, K := nextInt(), nextInt(), nextInt()
	T := make([][]string, H)
	for i:=0; i<H; i++{
		T[i] = make([]string, W)
		T[i] = chars(next())
	}
	ans := 0
	for bity := 0; bity < (1<<uint64(H)); bity++{
		for bitx := 0; bitx < (1<<uint64(W)); bitx++{
			tmpT := make([][]string, H)
			for i:=0; i<H; i++{
				tmpT[i] = append([]string{}, T[i]...)
			}
			for y := 0; y < H; y++{
				for x := 0; x<W; x++{
					if (bity >> uint64(y)) & 1 == 1 || (bitx >> uint64(x)) & 1 == 1{
						tmpT[y][x] = "赤"
					}
				}
			}
			count := 0
			for y:=0; y<H; y++{
				for x :=0; x<W; x++{
					if tmpT[y][x] == "#"{
						count++
					}
				}
			}
			if count == K{
				ans++
			}
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