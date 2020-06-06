package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

type Data struct {
	Id, P, Y int
	ANS      string
}

type DataS []Data

func (datas DataS) Len() int {
	return len(datas)
}

func (datas DataS) Swap(i, j int) {
	datas[i], datas[j] = datas[j], datas[i]
}

func (datas DataS) Less(i, j int) bool {
	if datas[i].P < datas[j].P {
		return true
	} else if datas[i].P > datas[j].P {
		return false
	} else {
		return datas[i].Y < datas[j].Y
	}
}

func (datas DataS) Format() map[int]string {
	count := make(map[int]int)
	for _, d := range datas {
		count[d.P]++
	}
	tmpIdx := 1
	tmpP := 1 // 問題文からして順番でいいはずだろうきっと多分
	for i := 0; i < len(datas); i++ {
		if datas[i].P > tmpP {
			tmpP = datas[i].P
			tmpIdx = 1
		}
		datas[i].ANS = fmt.Sprintf("%06d%06d", tmpP, tmpIdx)
		tmpIdx++
	}
	ret := make(map[int]string)
	for i := 0; i < len(datas); i++ {
		ret[datas[i].Id] = datas[i].ANS
	}
	return ret
}

func main() {
	buf := make([]byte, 1024*1024)
	sc.Buffer(buf, bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	defer out.Flush()
	_, M := nextInt(), nextInt()
	P, Y := make([]int, M), make([]int, M)
	DTS := make(DataS, M)
	for i := 0; i < M; i++ {
		P[i], Y[i] = nextInt(), nextInt()
		DTS[i] = Data{Id: i, P: P[i], Y: Y[i]}
	}
	sort.Sort(DTS)
	ans := DTS.Format()
	for i := 0; i < M; i++ {
		fmt.Fprintln(out, ans[i])
	}
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, _ := strconv.Atoi(next())
	return a
}

func nextInts(n int) []int {
	ret := make([]int, n)
	for i := 0; i < n; i++ {
		ret[i] = nextInt()
	}
	return ret
}
