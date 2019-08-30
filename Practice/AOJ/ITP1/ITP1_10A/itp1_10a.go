package main
import (
	"fmt"
	"math"
)

type Point struct{
	x,y  float64
}

func (p *Point)Dist(other_p Point)(ret float64){
	return math.Sqrt( (math.Pow((p.x-other_p.x), 2))+(math.Pow((p.y-other_p.y), 2)))
}

func main(){
	var x1, y1, x2, y2 float64
	fmt.Scan(&x1, &y1, &x2, &y2)
	p1 := Point{x:x1, y:y1}
	p2 := Point{x:x2, y:y2}
	fmt.Println(p1.Dist(p2))
}