// ぜんぜんわかりません
package main
import "fmt"
func main(){
	var A, B int
	MOD := int(1e9)+7
	fmt.Scan(&A, &B)
	dividers := make(map[int]int)
	for p := B+1; p<=A; p++{
		P := p
		for i := 2; i*i <= P; i++ {
			tmp := 0
			_P := P
			_pow := i
			for _P%i == 0 {
				_pow *= i
				tmp++
				_P /= i
			}
			if tmp > 0 {
				dividers[i] += tmp
				P /= (_pow / i)
			}
		}
		if P > 0 {
			dividers[P] += 1
		}
	}
	ans := 1
	for k, v := range dividers{
		if k==1{
			continue
		}
		ans*=(v+1)
		ans%=MOD
	}
	fmt.Println(ans)
}