package main
import (
	"fmt"
)

type Dice struct{
	/*
	こういう感じ
  		 ___
	____|_1_|_______
	|_4_|_2_|_3_|_5_|
		|_6_|
	*/
	Surface []int
}

func (d *Dice)Move(dir string){
	switch dir{
	case "W":
		d.Surface[0], d.Surface[2], d.Surface[5], d.Surface[3] = d.Surface[2], d.Surface[5], d.Surface[3], d.Surface[0]
	case "E":
		d.Surface[0], d.Surface[2], d.Surface[5], d.Surface[3] = d.Surface[3], d.Surface[0], d.Surface[2], d.Surface[5]
	case "N":
		d.Surface[0], d.Surface[4], d.Surface[5], d.Surface[1] = d.Surface[1], d.Surface[0],d.Surface[4], d.Surface[5]
	case "S":
		d.Surface[5], d.Surface[1], d.Surface[0], d.Surface[4] = d.Surface[1], d.Surface[0],d.Surface[4], d.Surface[5]	
	}
}

func (d *Dice)GetStatus(){
	doc := `              ____
 	 ____|_%02d_|_________
	|_%02d_|_%02d_|_%02d_|_%02d_|
	     |_%02d_|`
	fmt.Printf(doc, d.Surface[0], d.Surface[3], d.Surface[1], d.Surface[2], d.Surface[4], d.Surface[5])
	fmt.Println()
}

func main(){
	d := Dice{
		make([]int, 6),
	}
	for i:=0; i<6; i++{
		var n int
		fmt.Scan(&n)
		d.Surface[i] = n
	}
	var order string
	fmt.Scan(&order)
	for _, o := range []rune(order){
		d.Move(string(o))
		// fmt.Printf("move dir: %s\n", string(o))
		// d.GetStatus()
	}
	fmt.Println(d.Surface[0])
}