package main
import (
	"fmt"
)

var N int

var money = []int{10000, 5000, 2000, 1000, 500, 100, 50, 10,5, 1}

func main(){
	N = 45
	// 2段目から始める
	pascal := make([]int, 2)
	pascal[0], pascal[1] = 1, 1
	for i:=2; i<=N; i++{
		pascal = nextpascal(pascal)
		// fmt.Println(pascal, greedy(pascal))
	}
	fmt.Println(greedy(pascal))
}

// 先頭にnを追加したスライスを返す
func push(x []int, n int)(ret []int){
	ret = append(ret, n)
	for _, v := range x{
		ret = append(ret, v)
	}
	return
}

// 端に0追加してそこから前回のやつを足して作成
func nextpascal(x []int)(ret []int){
	nex1 := append(x, 0)
	nex2 := push(x, 0)
	for i:=0; i<len(x)+1; i++{
		ret = append(ret, nex1[i]+nex2[i])
	}
	return
}

func greedy(target []int)(ans int){
	for _, t := range target{
		for _, m := range money{
			ans+=t/m
			t%=m
		}
	}
	return ans
}