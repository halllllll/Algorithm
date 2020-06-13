// ABCBC ... 対応する3パターンのうち同じペアは2つ([C, C]と[B, B]) -> [A, C]の1つだけ互いに同じのにならないようにする 24*2
// ABCDCBC ... 4パターンのうち異なるペアは1つ 同上
// ABCDBCA ... 4パターンのうち異なるの2つ これだとなにをしてもだいじょうぶ
// -> 異なるペアが1つの場合のみなんか特殊なことする？

// ABBA ... 最初からペアのみ なんでもいい
// ABA ... 真ん中はどうやっても駄目
// みたいな感じで偶奇も見る

// ABCDBA ... 3パターンのうち異なるのは1箇所 このペアのみ考える
/// ABCDDAAA ... 4パターンのうち2箇所 なんでもよさそう

// 以上でやったならなぜかWAが6個ほど出た....
// AABBA ... 25+24+25+24+25 になってほしい
// ので,ペアが1つじゃなくてペアじゃないのが1つだったら、だったわ

package main

import "fmt"

func main() {
	var A string
	fmt.Scan(&A)
	S := make([]string, len(A))
	for i, c := range []rune(A) {
		S[i] = string(c)
	}
	pair := 0
	for i, j := 0, len(A)-1; i <= j; i, j = i+1, j-1 {
		if S[i] == S[j] {
			pair++
		}
	}
	length := len(A)
	if len(A)%2 == 1 {
		length += 1
	}
	if length/2 == pair {
		if len(A)%2 == 0 {
			// どれを変えてもいい*長さ
			fmt.Println(25 * len(A))
		} else {
			// 真ん中だけ無視して全部変えていい
			fmt.Println(25 * (len(A) - 1))
		}
	} else if length/2-pair == 1 {
		fmt.Println(24*2 + 25*(len(A)-2))
	} else {
		// もうなんでもいいよ
		fmt.Println(25 * len(A))
	}
}
