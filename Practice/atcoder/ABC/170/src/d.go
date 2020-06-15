// ソートすると、自分より小さいやつだけが対象となる
// 自分iを割り切るjがいたとき、jはiの約数のどれかである
// エラトステネス的に考えると、min(A)~max(A)までのすべてをA[i]の倍数で埋めていく感じになる？
// 1を含む場合・同じのを複数含む場合みたいな探索上しんどそうなやつは省く（ほかなんかある？）
// ↑まさかの「1を複数含む場合」があって無駄にWAを生やしてしまうの巻

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
	preA := nextInts(N)
	Distinct := make(map[int]bool)
	A := []int{}
	T := make([]bool, int(1e6+100)) // なんか知らんがRE出たのでたぶんこれが怪しいと踏んで余分に増やした
	sort.Ints(A)
	for _, a := range preA {
		if !Distinct[a] {
			Distinct[a] = true
			A = append(A, a)
		} else {
			// 同じのがあったらそれは駄目
			T[a] = true
		}
	}
	if A[0] == 1 {
		if N == 1 {
			fmt.Println(1)
			return
		} else {
			fmt.Println(0)
			return
		}
	}
	for _, a := range A {
		for x := a * 2; x <= int(1e6+10); x += a {
			T[x] = true
		}
	}
	ans := 0
	for _, a := range A {
		if T[a] == false {
			ans++
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
