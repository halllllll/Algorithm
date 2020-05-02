// 令和ABCだとB相当程度じゃね
package main
import (
	"fmt"
	"strings"
)
func main(){
	var N int
	fmt.Scan(&N)
	NG := make(map[string]bool)
	NG["a"] = true
	NG["i"] = true
	NG["u"] = true
	NG["e"] = true
	NG["o"] = true
	NG["y"] = true
	NG[","] = true
	NG["."] = true
	T := make(map[string]string)
	T["b"], T["c"] = "1", "1"
	T["d"], T["w"] = "2", "2"
	T["t"], T["j"] = "3", "3"
	T["f"], T["q"] = "4", "4"
	T["l"], T["v"] = "5", "5"
	T["s"], T["x"] = "6", "6"
	T["p"], T["m"] = "7", "7"
	T["h"], T["k"] = "8", "8"
	T["n"], T["g"] = "9", "9"
	T["z"], T["r"] = "0", "0"
	ans := []string{}
	for i:=0; i<N; i++{
		var C string
		fmt.Scan(&C)
		C = strings.ToLower(C)
		tmp := ""
		for _, c := range []rune(C){
			if _, ok := NG[string(c)]; !ok{
				tmp += T[string(c)]
			}
		}
		if tmp != ""{
			ans = append(ans, tmp)
		}
	}
	A := strings.Join(ans, " ")
	fmt.Println(A)
}