package main
import (
	"fmt"
)

var N = 30

// 7セグメントディスプレイの7箇所の位置や構造とかはどうでもよくて、各数値に対して点灯する量だけ対応してればよい
// あとは時間だがふつうにforで回せばいいや。一桁の場合はゼロ埋めを考える

var Display map[string]int

func main(){
	Display = map[string]int{
		"1": 2,
		"2": 5,
		"3": 5,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 3,
		"8": 7,
		"9": 6,
		"0": 6,
	}
	cnt := 0
	for h :=0; h<=23; h++{
		for m:=0; m<=59; m++{
			for s:=0; s<=59; s++{
				sh := fmt.Sprintf("%02d", h)
				sm := fmt.Sprintf("%02d", m)
				ss := fmt.Sprintf("%02d", s)
				// fmt.Printf("time: %s:%s:%s\n", sh, sm, ss)
				if f(sh)+f(sm)+f(ss)==N{
					cnt++
				}				
			}
		}
	}
	fmt.Println(cnt)
}

func f(s string)(ret int){
	for _, v := range []rune(s){
		ret += Display[string(v)]
	}
	return 
}