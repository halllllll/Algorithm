package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

func main() {
	sc.Split(bufio.ScanWords)
	defer out.Flush() // !!!!caution!!!! you must use Fprint(out, ) not Print()
	/* --- code --- */
	// 思考レベル1: ビットごとの排他的論理和たらいう概念を理解
	// 思考レベル2: 実験すると最下位ビットが立ってると奇数なので、自分が奇数のとき、両隣のうちいずれか片方が奇数で他方が偶数である必要がある。自分が偶数のとき、両方が奇数もしくは偶数である必要がある
	// 並べると偶奇奇偶奇奇偶奇奇....で2/3が奇数、1/3が偶数になる。この場合は長さが3の倍数でなくてはならない
	// あるいは偶偶偶偶偶偶偶...でぜんぶ偶数の場合である
	// 思考レベル4: 数の大きさがどう関係するのかわからなくて詰み
	// 偶数だけの場合は2 6 0 4とかだと(4+6)=(100+110)=100で駄目 (2+0)=(10+0)=0で駄目 (4+0)=(100+0)=100で駄目、全部ダメじゃねぇか
	// 2 2 2 2だと(10+10)=10でおｋ つまり全部同じ数字じゃないと駄目
	//  偶奇奇...も同じだろうか？ 2 5 5 2 5 5 だと(10+101)=111で駄目だし(10+10)=10で当然5にならんので駄目
	// 2 3 1 2 1 3だと(11+11)=0で駄目 (10+1)=11でおｋ(11+10)=1でおｋ [2 3 1]と[3 1 2]がおｋ
	// なので 2 3 1 2 3 1 はおｋ
	// 数を変えて 6 3 7だと(111+11)=100で駄目 (110+111)=1で駄目 (110+11)=1で駄目 全部駄目じゃん
	// 差が1ならいいのか？ 6 5 7だと(110+111)=1で駄目 はい駄目
	// 2を加えたもの 4 5 3だと(100+11)==(111)で駄目 はい駄目
	// もうこれ2 3 1以外のやつ存在しないのでは（理屈は知らん） あるいは 0 同じ奇数 同じ奇数
	// ここまで考えて2時間くらいでつまらなくなった
}

// -*-*-*-*-*-*-*-*-
// * I/O utilities *
// -*-*-*-*-*-*-*-*-

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func nextFloat64() float64 {
	a, _ := strconv.ParseFloat(next(), 64)
	return a
}

func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}
func nextFloats(n int) []float64 {
	ret := make([]float64, n)
	for i := 0; i < n; i++ {
		ret[i] = nextFloat64()
	}
	return ret
}
func nextStrings(n int) []string {
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		ret[i] = next()
	}
	return ret
}

func chars(s string) []string {
	ret := make([]string, len([]rune(s)))
	for i, v := range []rune(s) {
		ret[i] = string(v)
	}
	return ret
}

func PrintOut(src interface{}, joinner string) {
	switch reflect.TypeOf(src).Kind() {
	case reflect.Slice:
		s := reflect.ValueOf(src)
		for idx := 0; idx < s.Len(); idx++ {
			fmt.Fprintf(out, "%v", s.Index(idx))
			if idx < s.Len()-1 {
				fmt.Fprintf(out, "%s", joinner)
			} else {
				fmt.Fprintln(out)
			}
		}
	default:
		fmt.Fprintln(out, "fuck")
	}
}

// -*-*-*-*-*-*-*-*-
// * tool snippets *
// -*-*-*-*-*-*-*-*-
func duplicate2Int(base [][]int) (ret [][]int) {
	ret = make([][]int, len(base))
	for i, v := range base {
		ret[i] = append([]int{}, v...)
	}
	return
}

func min(a, b interface{}) interface{} {
	x, y := toFloat64(a), toFloat64(b)
	if x < y {
		return a
	} else {
		return b
	}
}

func max(a, b interface{}) interface{} {
	x, y := toFloat64(a), toFloat64(b)
	if x > y {
		return a
	} else {
		return b
	}
}

func toFloat64(v interface{}) float64 {
	r := reflect.ValueOf(v)
	if r.IsValid() {
		switch r.Kind() {
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64,
			reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64,
			reflect.Float32, reflect.Float64:
			var x float64
			return r.Convert(reflect.TypeOf(x)).Interface().(float64)
		default:
			return 0

		}
	}
	return 0
}

// -*-*-*-*-*-*-*-*-*-*-*-*-*-
// * Algorithms Utility Zone *
// -*-*-*-*-*-*-*-*-*-*-*-*-*-

// -*-*-*-*-*-*-*-
// * 1. nibutan  *
// -*-*-*-*-*-*-*-
func lower_bound(arr []int, target int) int {
	l, r := 0, len(arr)
	for l < r {
		mid := (l + r) / 2
		if arr[mid] < target {
			l = mid + 1
		} else {
			r = mid
		}
	}
	return l
}

func upper_bound(arr []int, target int) int {
	l, r := 0, len(arr)
	for l < r {
		mid := (l + r) / 2
		if target < arr[mid] {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}

// *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
// * math flavor typical theories *
// *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
func gcd(a, b int) int {
	if a > b {
		return gcd(b, a)
	}
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

func pow(a, b int) (ret int) {
	ret = a
	// 10^2 = 100ってことは10に10を1回掛けることだね
	// なので初期値を含めると上限b-1未満
	for i := 0; i < b-1; i++ {
		ret *= a
	}
	return
}

func powMod(n, m, mod int) (ret int) {
	ret = 1
	for m > 0 {
		if m&1 == 1 {
			ret *= n
			ret %= mod
		}
		n *= n
		n %= mod
		m >>= 1
	}
	return ret
}

func ncr(n, r int) int {
	// せいぜいn<10^2くらいの精度しかなくない？
	res := 1
	for i := 1; i <= r; i++ {
		res = res * (n - i + 1) / i
	}
	return res
}

func ncrMod(n, r, mod int) int {
	// 呼び出すたびにテーブルを作るのは愚です（どうしようかね）
	_n := 1000000
	g1 := make([]int, _n+1)
	g1[0], g1[1] = 1, 1
	g2 := make([]int, _n+1)
	g2[0], g2[1] = 1, 1
	inverse := make([]int, _n+1)
	inverse[0], inverse[1] = 0, 1
	for i := 2; i <= _n; i++ {
		g1[i] = (g1[i-1] * i) % mod
		inverse[i] = mod - inverse[mod%i]*(mod/i)%mod
		g2[i] = (g2[i-1] * inverse[i]) % mod
	}

	return g1[n] * (g2[r] * g2[n-r] % mod) % mod
}

func next_permutation(arr []int) func() []int {
	/*
		how to use it:
			this is a generator, so should be invoked such as below example.

			"""code"""
			np := next_permutation(arr)
			for{
				lis := np()
				if len(lis) == 0{
					break
				}
				fmt.Println(lis)
			}
			"""code end"""
	*/
	first := true
	ret := append([]int{}, arr...)
	_next_permutation := func() []int {
		if first {
			first = false
			return arr
		}
		n := len(ret)
		for i := n - 2; i >= 0; i-- {
			if ret[i] < ret[i+1] {
				j := n
				for {
					j -= 1
					if ret[i] < ret[j] {
						break
					}
				}
				ret[i], ret[j] = ret[j], ret[i]
				for k := n - 1; i < k; i, k = i+1, k-1 {
					ret[i+1], ret[k] = ret[k], ret[i+1]
				}
				return ret
			}
		}
		return []int{}
	}
	return _next_permutation
}
