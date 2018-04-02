package main

import (
	"fmt"
	"math"
)

type Point struct {
	X, Y float64
}

type Calc interface {
	Dist(p *Point) float64
}

func (p *Point) Dist(other_p *Point) (ret float64) {
	ret = math.Sqrt(math.Pow(p.X-other_p.X, 2.0) + math.Pow(p.Y-other_p.Y, 2.0))
	return
}

var Points []Point

func main() {
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var x, y float64
		fmt.Scan(&x, &y)
		newp := Point{x, y}
		Points = append(Points, newp)
	}
	var maxdist float64
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if i < j {
				maxdist = math.Max(maxdist, Points[i].Dist(&Points[j]))
			}
		}
	}
	fmt.Println(maxdist)
}
