package main
import (
	"fmt"
	"math"
	"bufio"
	"os"
	"strconv"
)

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	for scanner.Scan(){
		n, _ := strconv.Atoi(scanner.Text())
		if n==0{
			break
		}
		ns := make([]int, n)
		for i:=0; i<n; i++{
			scanner.Scan()
			a, _ := strconv.Atoi(scanner.Text())
			ns[i] = a
		}
		stddev := math.Sqrt(disperse(ns, average(ns)))
		fmt.Println(stddev)
	}
}

func disperse(ns []int, m float64)(ret float64){
	for _, v := range ns{
		ret += math.Pow(float64(v)-m, 2.0)
	}
	return ret/float64(len(ns))
}

func average(ns []int)(ret float64){
	for _, v := range ns{
		ret+=float64(v)
	}
	return ret/float64(len(ns))
}