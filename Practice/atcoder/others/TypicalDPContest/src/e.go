// ペロッこれは桁DP

package main

import (
	"fmt"
	"strconv"
)

var D int
var S []string
var MOD int
var memo map[int]map[bool]map[int]int

func main() {
	var SS string
	memo = make(map[int]map[bool]map[int]int)
	fmt.Scan(&D, &SS)
	S = make([]string, len(SS))
	for i, c := range []rune(SS) {
		S[i] = string(c)
	}
	MOD = int(10e9) + 7
	// 漸化式たてた -> じゃあループにできるね(????)
	// 漸化式以下
	// DP[i][b][c] := 先頭からi桁までみたとき、各桁の総和をDで割ったあまりをcとしたときの数
	// DP[i][false][c] -> 先頭からi桁目まででS以下確定
	// DP[i][true][c] -> 先頭からi桁目までSと一致
	// DP[0][false][0] := 0
	// 上以外: 適当に-INFとでもしておけ
	//
	fmt.Println(rec(0, false, 0) - 1)
	// aaa := make(map[bool]map[int]int)
	// aa := make(map[int]int)
	// aa[100] = 2
	// aaa[false] = aa
	// memo[0] = aaa
	// fmt.Println(memo)
	// fmt.Println(memo[0][false][100])
}

func rec(i int, smaller bool, cur int) int {
	if _, ok := memo[i][smaller][cur]; ok {
		fmt.Println("yes")
		return memo[i][smaller][cur]
	}
	if i == len(S) {
		if cur%D == 0 {
			return 1
		}
		return 0
	}
	ret := 0
	limit := 10
	n, _ := strconv.Atoi(S[i])
	if smaller == false {
		limit = n + 1
	}
	for j := 0; j < limit; j++ {
		nex := cur*10 + j
		nex %= D
		ret += rec(i+1, smaller || j < n, nex)
	}
	memomemomemo := make(map[int]int)
	memomemomemo[cur] = ret
	memomemo := make(map[bool]map[int]int)
	memomemo[smaller] = memomemomemo
	memo[i] = memomemo
	return memo[i][smaller][cur]
}
