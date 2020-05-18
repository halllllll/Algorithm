// キューもってなくてBFSできないのでDFSでやります
// ゴールきまってんの忘れてた...
package main

import (
	"fmt"
	"strconv"
)

type Q struct {
	X, Y int
}

type Queue struct {
	queue []Q
}

// Enqueue ... the so-called enqueue
func (q *Queue) Enqueue(x Q) {
	q.queue = append(q.queue, x)
}

// Dequeue ... the so-called dequeue
func (q *Queue) Dequeue() (ret Q) {
	ret, q.queue = q.queue[0], q.queue[1:]
	return
}

// Len ... return length of queue
func (q *Queue) Len() (ret int) {
	return len(q.queue)
}

func main() {
	var R, C int
	fmt.Scan(&R, &C)
	var Sy, Sx, Gy, Gx int
	fmt.Scan(&Sy, &Sx, &Gy, &Gx)
	Sy--
	Sx--
	Gx--
	Gy--
	T := make([][]string, R)
	for i := 0; i < R; i++ {
		var line string
		fmt.Scan(&line)
		T[i] = make([]string, C)
		for j, c := range []rune(line) {
			T[i][j] = string(c)
		}
	}
	T[Sy][Sx] = "0"

	steps := []int{0, 1, 0, -1, 0}
	var que Queue
	que.Enqueue(Q{X: Sx, Y: Sy})
	for que.Len() > 0 {
		cur := que.Dequeue()
		curN, _ := strconv.Atoi(T[cur.Y][cur.X])
		for i := 0; i < 4; i++ {
			nx, ny := cur.X+steps[i], cur.Y+steps[i+1]
			if 0 <= nx && nx < C && 0 <= ny && ny < R && T[ny][nx] != "#" {
				// 未踏なら歩く、更新できるなら更新する
				if T[ny][nx] == "." {
					T[ny][nx] = strconv.Itoa(curN + 1)
					que.Enqueue(Q{X: nx, Y: ny})
				} else {
					nexN, _ := strconv.Atoi(T[ny][nx])
					if nexN > curN+1 {
						// 更新できるよ
						T[ny][nx] = strconv.Itoa(curN + 1)
						que.Enqueue(Q{X: nx, Y: ny})
					}
				}
			}
		}
	}
	ans, _ := strconv.Atoi(T[Gy][Gx])
	fmt.Println(ans)
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
