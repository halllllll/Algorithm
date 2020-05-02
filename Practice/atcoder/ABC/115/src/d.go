// i層目のバーガー
// B + [i-1層目のバーガー] + P + [i-1層目のバーガー] + B
// i層目の層の総数 3+2*[i-1層目の層の総数]
// i層目のPの総数 1+2*[i-1層目のPの総数]

// なんか何回やってもあらかじめi層目の層の総数を計算しておくみたいなのしか思いつかん

package main
import "fmt"
var nth, pth []int
func main(){
	var N, X int
	fmt.Scan(&N, &X)
	nth = make([]int, 51)
	pth = make([]int, 51)
	nth[0], pth[0] =1, 1
	for i:=1; i<=50; i++{
		nth[i] = 3+2*nth[i-1]
		pth[i] = 1+2*pth[i-1]
	}
	fmt.Println(rec(N, X))
}


func rec(n, x int)int{
	if x == 0 {
		return 0
	}
	if n == 0{
		if x == 0{
			return 0
		}
		return 1
	}
	if 2*x < nth[n]{
		return rec(n-1, x-1)
	}else{
		// これが鬼 第2引数を間違えていた 脳死で2*x-nth[n]としていた
		// 半分より左側をごっそりけずるのでnth[n-1]としなければならない
		return pth[n-1] + rec(n-1, x-2-nth[n-1]) + 1
	}
	fmt.Println("ファーーー")
	return -9999999999999999
}