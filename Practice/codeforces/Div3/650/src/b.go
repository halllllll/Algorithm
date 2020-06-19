// これ面白いなー
// 01010101...になればよくて、今みてるのが違った場合、今見てるのから右側で最も近い「正しいやつ」を持ってくることを考える。
// これは結果的にはswapで、試行的には差分
// しゃくとりっぽい気がする
// もちろん01の終始が合わなければ0なので

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
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	T := nextInt()
	for i := 0; i < T; i++ {
		N := nextInt()
		tmpA := nextInts(N)
		A := make([]int, N)
		odd, even := 0, 0
		for j, k := range tmpA {
			A[j] = k % 2
			if A[j]%2 == 0 {
				even++
			} else {
				odd++
			}
		}
		// fmt.Printf("%vを1-0にして%v\neven, odd = %d, %d\n", tmpA, A, even, odd)
		if N%2 == 0 && even != odd {
			fmt.Fprintln(out, -1)
			continue
		} else if N%2 == 1 && even-odd != 1 {
			// ex) N=1 だと（0 orderなので）even=1(idx=0), odd=0
			// ex) N=3 だと even=2(idx=0,2), odd=1(idx=1)
			fmt.Fprintln(out, -1)
			continue
		}
		if N%2 == 0 {
			A = append(A, 0)
		} else {
			A = append(A, 1)
		}
		// fmt.Fprintf(out, "探索用 %v\n", A)
		ans := 0
		for l := 0; l < N; l++ {
			if A[l] == l%2 {
				continue
			}
			r := l + 1
			for r < N && A[r] == r%2 {
				r++
			}
			A[r], A[l] = A[l], A[r]
			// fmt.Fprintf(out, "l=%dとr=%dを交換すればいいってこと？？\n", l, r)
			ans += r - l
		}
		// fmt.Fprintf(out, "探索後: %v\n", A)
		fmt.Fprintln(out, ans)
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

// 4
// 4
// 3 2 7 6
// 3
// 3 2 6
// 1
// 7
// 7
// 4 9 2 1 18 3 0
