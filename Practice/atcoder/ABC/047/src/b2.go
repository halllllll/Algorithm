// 1,2はxだけ、3,4はyだけみればいい
// 1のうち最大値、2のうち最小値、3のうち最大値、4のうち最小値だけみればいい
// (min(w, min(x2))-max(0, max(x1)))*(min(h, min(y4))-max(0, max(y3)))
// ex: sample1) (w-2)*(3-0) = 3*3 = 9
package main
import "fmt"
var w, h, n int
func main(){
	fmt.Scan(&w, &h, &n)
	maxX1, minX2, maxY3, minY4 := 0, w, 0, h
	for i:=0; i<n; i++{
		var x, y, a int
		fmt.Scan(&x, &y, &a)
		if a == 1{
			if maxX1 < x{
				maxX1 = x
			}
		}else if a == 2{
			if minX2 > x{
				minX2 = x
			}
		}else if a == 3{
			if maxY3 < y{
				maxY3 = y
			}
		}else if a == 4{
			if minY4 > y{
				minY4 = y
			}
		}
	}
	if maxX1 > minX2 || maxY3 > minY4{
		fmt.Println(0)
	}else{
		fmt.Println((minX2-maxX1)*(minY4-maxY3))
	}
}