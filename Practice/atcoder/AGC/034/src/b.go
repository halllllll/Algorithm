// 愚直どうすか...（計算量の見積もりがわからん）
// 完成形はA...Xの部分が(Aの数)*(Bの数)となってるっぽいのでそうする感じでやってみる
// ↑この探索にはしゃくとりが使えそうなのでそうする
// （いまおもったんすがにぶたんで良い気がするが。。。)

package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	SS := make([]string, len(S))
	for i, c := range []rune(S) {
		SS[i] = string(c)
	}
	T := []string{}
	for i := 0; i < len(SS)-1; {
		if SS[i] == "B" && SS[i+1] == "C" {
			T = append(T, "X")
			i += 2
		} else {
			T = append(T, SS[i])
			i++ 
		}
	}
	fmt.Println(T)
	ans := 0
	// for {
	// 	flag := true
	// 	for i := 0; i < len(T)-1; i++ {
	// 		if T[i] == "A" && T[i+1] == "X" {
	// 			ans++
	// 			T[i], T[i+1] = T[i+1], T[i]
	// 			flag = false
	// 		}
	// 	}
	// 	if flag {
	// 		break
	// 	}
	// }
	// 番兵
	T = append(T, "死")
	r := 0
	for l := 0; l < len(T); {
		if T[l] != "A" {
			l++
			continue
		}
		r = l
		for r < len(T) && T[r] == "A" {
			r++
		}
		if T[r] != "X" {
			fmt.Printf("l, r = %d, %d の範囲で存在しなかったので仕切り直し\n", l, r)
			fmt.Println(T[l:r])
			l = r - 1
		} else {
			aLen := r - l // 連続したAの数
			for r < len(T) && T[r] == "X" {
				r++
			}
			fmt.Printf("これな l, mid, r = %d, %d, %d, %v\n", l, aLen, r, T[l:r])
			fmt.Printf("追加: %d\n", aLen*(r-l-aLen))
			ans += aLen * (r - l - aLen)
			// SS[l], SS[r-1] = SS[r-1], SS[l]
			l = r - 1
		}
	}
	fmt.Println(T)
	fmt.Println(ans)
}

// AAABCBCCCBABABCBAABCCCBACBABCABBACABCABAABCC (13)
// AABCBCAABCBCBACCABC -> X A A X X A A X B A C C X A
