// https://kenkoooo.com/atcoder/#/contest/show/a9a7a4e2-047d-4784-8e13-668951991a1d からきました
// ふたつ先までのdfsでいいので間に合いそう
// 1をスタートにして隣接してるノードから更にひとつだけ伸ばし、Nかどうかみるだけ
package main
import "fmt"
var n, m int
var graph [][]int
func main(){
	fmt.Scan(&n, &m)
	graph = make([][]int, n)
	for i:=0; i<n; i++{
		graph[i] = []int{}
	}
	for i:=0; i<m; i++{
		var a, b int
		fmt.Scan(&a, &b)
		graph[a-1] = append(graph[a-1], b-1)
		graph[b-1] = append(graph[b-1], a-1)
	}
	for _, relayPoint := range graph[0]{
		for _, goal := range graph[relayPoint]{
			if goal == n-1{
				fmt.Println("POSSIBLE")
				return
			}
		}
	}
	fmt.Println("IMPOSSIBLE")
}