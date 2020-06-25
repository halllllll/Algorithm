// 各桁の和の最大値は9*18くらいなのでこれで探索できるか？

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	limit := digitSum(N)
	for i := 1; i <= limit; i++ {
		// 各桁の総和がiなる かつ N以下 かつ 桁数がN以下 なるやつ
	}
}

func gen(x int) func() int {
	length := digitLength(x)
	sum := digitSum(x)
	arr := []int{}
	for i := 1; i < 10; i++ {
		if i <= x {
			arr = append(arr, i)
		}
	}
	ret := func() int {
		nextRet := []int{}
		for _, a := arr{
			return a
		}
	}
	return ret
}

func digitLength(x int) int {
	ret := 1
	for x > 0 {
		ret++
		x /= 10
	}
	return ret
}

func digitSum(x int) int {
	ret := 0
	for x > 0 {
		ret += x % 10
		ret /= 10
	}
	return ret
}
