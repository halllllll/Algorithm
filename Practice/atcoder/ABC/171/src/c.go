// 1000000000000001でz11文字 -> i文字目はたかだか26種類（たかだかじゃねぇよ）
// -> で、全探索は無理なので数式でやる
// 世の中にABCの三文字しかないときに長さ3文字を作ろうとしたときにできる文字列を小さい順に並べたとき（早い話がABCから3つ取るpermutation）、全部で27通りであり、
// 左から数えて「1文字目がAなるのは前半の1/3(1~9)」「Bは次の1/3(10~18)」「Cは最後の1/3（19~27）」
// 2文字目がAなるのはそれぞれ「前半1/3の中の前半1/3」「次の1/3の前半1/3」「最後の1/3の前半1/3」となる
// これをなんか愚直に範囲を狭めてやろうとしたら無限にバグったのでポンコツ
// これを数式でやるのがポイント
// 26で割ったあまりをどんどこしていく感じ
// ゆうてなんかよくわからんかったのですげぇ雑にアドホックにやった

package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scan(&N)
	alphabets := []string{"z", "a"}
	for len(alphabets) < 26 {
		t := alphabets[len(alphabets)-1]
		ts := string(t[0] + 1)
		alphabets = append(alphabets, ts)
	}
	x := N
	ans := []string{}
	for x > 0 {
		ans = append(ans, alphabets[x%26])
		x--
		x /= 26
	}
	for i := len(ans) - 1; i >= 0; i-- {
		fmt.Printf("%s", ans[i])
	}
	fmt.Println()
}
