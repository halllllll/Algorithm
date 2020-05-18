// 偶奇で数えて登場回数最大以外を書き換えるんじゃないの
// 書き換える先が偶奇で同じになってしまったら二番目に大きいやつで勝負してぶつける
// コーナーケース注意（二番目が存在しない）
// 実装がクソ
package main

import (
	"fmt"
	"sort"
)

type KV struct {
	k, v int
}

type KVS []KV

func (kvs KVS) Len() int {
	return len(kvs)
}

func (kvs KVS) Less(i, j int) bool {
	return kvs[i].v > kvs[j].v
}

func (kvs KVS) Swap(i, j int) {
	kvs[i], kvs[j] = kvs[j], kvs[i]
}

func main() {
	var N int
	fmt.Scan(&N)
	evenMap, oddMap := make(map[int]int), make(map[int]int)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if i%2 == 0 {
			oddMap[V]++
		} else {
			evenMap[V]++
		}
	}
	var evenKVSS, oddKVSS KVS
	for k, v := range evenMap {
		evenKVSS = append(evenKVSS, KV{k: k, v: v})
	}
	for k, v := range oddMap {
		oddKVSS = append(oddKVSS, KV{k: k, v: v})
	}
	sort.Sort(evenKVSS)
	sort.Sort(oddKVSS)
	if len(evenKVSS) == 1 && len(oddKVSS) == 1 {
		if evenKVSS[0].k == oddKVSS[0].k {
			// 登場する数が全て同じなのでどっちかをまるっと変更する
			fmt.Println(N / 2)
		} else {
			// そのまんまでいい
			fmt.Println(0)
		}
	} else if len(evenKVSS) == 1 || len(oddKVSS) == 1 {
		// 2つ以上あるやつを変更したいがこれもkで決まるな...めんどくせ
		if evenKVSS[0].k == oddKVSS[0].k {
			if len(evenKVSS) == 1 {
				fmt.Println(N/2 - oddKVSS[1].v)
			} else {
				fmt.Println(N/2 - evenKVSS[1].v)
			}
		} else {
			if len(evenKVSS) == 1 {
				fmt.Println(N/2 - oddKVSS[0].v)
			} else {
				fmt.Println(N/2 - evenKVSS[0].v)
			}
		}
	} else {
		if evenKVSS[0].k == oddKVSS[0].k {
			// 数が被るので少ないほうをまるっと変更する
			if evenKVSS[0].v == oddKVSS[0].v {
				// しょうがないので二番目に大きい方で比較する
				if evenKVSS[1].k == oddKVSS[1].k {
					// どっちかを最大、他方を二番目のやつを採用する
					fmt.Println(N/2 - evenKVSS[0].v + N/2 - oddKVSS[1].v)
				} else {
					// 二番目のやつの登場回数が多い方を採用する
					if evenKVSS[1].v > oddKVSS[1].v {
						fmt.Println(N/2 - evenKVSS[1].v + N/2 - oddKVSS[0].v)
					} else if evenKVSS[1].v < oddKVSS[1].v {
						fmt.Println(N/2 - evenKVSS[0].v + N/2 - oddKVSS[1].v)
					} else {
						// なんだこれ
						// どっちかを最大、他方を二番目におおきいやつ
						fmt.Println(N/2 - evenKVSS[0].v + N/2 - oddKVSS[1].v)
					}
				}
			} else {
				// 登場回数の少ない方は二番目のやつを採用
				if evenKVSS[0].v > oddKVSS[0].v {
					fmt.Println(N/2 - evenKVSS[0].v + N/2 - oddKVSS[1].v)
				} else {
					fmt.Println(N/2 - evenKVSS[1].v + N/2 - oddKVSS[0].v)
				}
			}
		} else {
			// どちらも最大のやつはかぶらないのでどちらもそれ以外のやつを最大のやつに合わせる
			fmt.Println(N/2 - evenKVSS[0].v + N/2 - oddKVSS[0].v)
		}
	}
}

// 8
// 2 5 2 9 1 5 3 5
