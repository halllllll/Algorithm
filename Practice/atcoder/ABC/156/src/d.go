// ncrModせいぜい10^6とかだった気がするので無理
// これは悔しいですね クソが

package main
import "fmt"
func main(){
	var N, A, B int
	fmt.Scan(&N, &A, &B)
	MOD := int(1e9)	+ 7
  // repModP、「どっちも選ばない」を含むのでそれを-1
	ans := (repModP(2, N, MOD) - 1 - nCrModP(N, A, MOD) - nCrModP(N, B, MOD))%MOD
	if ans < 0{
		ans += MOD
	}
	fmt.Println(ans)
}

func repModP(a, n, mod int)int{
	if n==1{
		return a % mod
	}
	if n % 2 == 1{
		return a * repModP(a, n-1, mod) % mod
	}
	ret := repModP(a, n/2, mod) % mod
	ret = (ret * ret) % mod
	if ret < 0{
		ret += mod
	}
	return ret
}

func nCrModP(n, r, mod int)int{
	ret := 1
	for i:=n-r+1; i<=n; i++{
		ret *= i
		ret %= mod
	}
	for i:=2; i<=r; i++{
		ret *= repModP(i, mod-2, mod)
		ret %= mod
	}
	ret %= mod
	if ret < 0{
		ret += mod
	}
	return ret
}