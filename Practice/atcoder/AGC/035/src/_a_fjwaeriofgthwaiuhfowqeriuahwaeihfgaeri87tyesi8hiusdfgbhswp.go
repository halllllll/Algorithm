// 思考レベル1: ビットごとの排他的論理和たらいう概念を理解 2つのビットのうちいずれかが1でいずれかが0
// 思考レベル2: 実験すると最下位ビットが立ってると奇数なので、自分が奇数のとき、両隣のうちいずれか片方が奇数で他方が偶数である必要がある。自分が偶数のとき、両方が奇数もしくは偶数である必要がある
// 並べると偶奇奇偶奇奇偶奇奇....で2/3が奇数、1/3が偶数になる。この場合は長さが3の倍数でなくてはならない
// あるいは偶偶偶偶偶偶偶...でぜんぶ偶数の場合である
// 思考レベル3: 同じ数でないといけなさそう、これは偶奇交じる場合もそう
// まとめると、登場する偶数は1種類、奇数は2種類であり、総数が偶:奇=1:2になっていないと駄目そう
// あるいはすべて同じ偶数,または0と0以外の同一の偶数が1:2

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	oddsT, evensT := make(map[int]int), make(map[int]int)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if V%2 == 0 {
			evensT[V] += 1
		} else {
			oddsT[V] += 1
		}
	}
	if len(oddsT) == 0 {
		if len(evensT) > 2 {
			fmt.Println("No")
		} else if _, ok := evensT[0]; ok && len(evensT) == 1 {
			fmt.Println("Yes")
		} else if len(evensT) == 2 {
			keys := []int{}
			for k, _ := range evensT {
				keys = append(keys, k)
			}
			if 2*evensT[keys[0]] == evensT[keys[1]] || evensT[keys[0]] == 2*evensT[keys[1]] {
				fmt.Println("Yes")
			} else {
				fmt.Println("No")
			}
		} else {
			fmt.Println("No")
		}
	} else if N%3 != 0 {
		fmt.Println("No")
	} else if len(oddsT) == 2 && len(evensT) == 1 {
		keys := []int{}
		for k, _ := range oddsT {
			keys = append(keys, k)
		}
		if oddsT[keys[0]]+oddsT[keys[1]] == 2*N/3 {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	} else {
		fmt.Println("No")
	}
}
