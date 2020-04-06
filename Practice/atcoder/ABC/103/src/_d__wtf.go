// これは「言語アプデしたらしいしやってみるか〜」と思ってやったら過去問はアプデ対象外らしくて死んだだけのコードです

package main
import (
	"fmt"
	"sort"
)

type Interval struct{
	L, R int
}

var n, m int
var a []Interval

func main(){
	fmt.Scan(&n, &m)
	a = make([]Interval, m)
	for i:=0; i<m; i++{
		var x, y int
		fmt.Scan(&x, &y)
		interval := Interval{L: x, R: y}
		a[i] = interval
	}
	sort.Slice(a, func(i, j int)bool{
		return a[i].R < a[j].R
	})
	ans := 0
	// 前回:今=i:jってしたときa[i].R>a[j].Lならやんなくていい 違ったらやんないといけない
	// ????????????????????????????????????????????????????????
	// 理屈ではわかった気になるがぜんぜん理解できてない 
	ir := 0
	for _, interval := range a{
		if ir < interval.L{
			ans += 1
			ir = interval.R-1
		}
	}
	fmt.Println(ans)
}