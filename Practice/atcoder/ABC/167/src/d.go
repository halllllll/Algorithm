// ダブリングとかいうの初めて知った
package main

import "fmt"

func main() {
	var N int
	var K int64
	fmt.Scan(&N, &K)
	A := make([]int, N+1)
	Double := make([][]int, 62) // 10^18≒2^60
	for i := 0; i < len(Double); i++ {
		Double[i] = make([]int, N+1)
	}
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i+1] = V
		Double[0][i+1] = V
	}
	for i := 1; i < len(Double); i++ {
		for j := 1; j < N+1; j++ {
			Double[i][j] = Double[i-1][Double[i-1][j]]
		}
	}

	// わからん?>??>????>???>??
	// なんかデカい桁からみる==Kを2進表記した最上位桁からみるをして、ビットが立っていれば採用してるっぽいんだけど
	// なんでそれを採用したらいい具合になるのかさっっっっっっぱりわからん
	v := 1 
	for i := len(Double) - 1; i >= 0; i-- {
		if (K>>int64(i))&1 == 1 {
			v = Double[i][v]
		}
	}
	fmt.Println(v)
}
int v = 0;
for (int i=D-1; i>=0; i++){
	ll l = 1ll<<i;
	if(l<=k){
		v = to[i][v];
		k -= l;
	}
}
count << v+1 << endl;

// 10 5
// 4 7 2 8 5 3 4 7 2 1

// 12 6
// 8 4 2 10 6 9 1 11 2 12 6 5

// 8 4
// 4 5 8 2 7 3 6 7
