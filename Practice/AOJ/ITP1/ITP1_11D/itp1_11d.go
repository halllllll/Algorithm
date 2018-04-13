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

func (d *Dice)Move(dir string, n int){
	n%=4
	switch dir{
	case "W":
		for i:=0; i<n; i++{
			d.Surface[0], d.Surface[2], d.Surface[5], d.Surface[3] = d.Surface[2], d.Surface[5], d.Surface[3], d.Surface[0]
		}
	case "E":
		for i:=0; i<n; i++{
			d.Surface[0], d.Surface[2], d.Surface[5], d.Surface[3] = d.Surface[3], d.Surface[0], d.Surface[2], d.Surface[5]
		}
	case "N":
		for i:=0; i<n; i++{
			d.Surface[0], d.Surface[4], d.Surface[5], d.Surface[1] = d.Surface[1], d.Surface[0],d.Surface[4], d.Surface[5]
		}
	case "S":
		for i:=0; i<n; i++{
			d.Surface[5], d.Surface[1], d.Surface[0], d.Surface[4] = d.Surface[1], d.Surface[0],d.Surface[4], d.Surface[5]	
		}
	}
}

func (d *Dice)Roll(dir string, n int){
	n%=4	// べつにいらんけど一周したら元にもどるので
	switch dir{
	case "R":
		for i:=0; i<n; i++{
			d.Surface[3], d.Surface[1], d.Surface[2], d.Surface[4] = d.Surface[1], d.Surface[2], d.Surface[4], d.Surface[3]
		}	
	case "L":
		for i:=0; i<n; i++{
			d.Surface[3], d.Surface[1], d.Surface[2], d.Surface[4] = d.Surface[4], d.Surface[3], d.Surface[1], d.Surface[2]
		}
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

func (d *Dice)IsEqual(other_d Dice)(ret bool){
	if len(d.Surface) != len(other_d.Surface){
		return false
	}
	for i, v := range d.Surface{
		if v!=other_d.Surface[i]{
			return false
		}
	}
	return true
}

func main(){
	var n int
	fmt.Scan(&n)

	Dices := make([]Dice, n)
	for i:=0; i<n; i++{
		d := Dice{}
		for x:=0; x<6; x++{
			var f int
			fmt.Scan(&f)
			d.Surface = append(d.Surface, f)
		}
		Dices[i] = d
	}

	roll_order := []string{"R", "L"}
	direction_order := []string{"N", "W", "E", "S"}
	ans := true

	CHECK:
		for x:=0; x<n; x++{
			x_d := Dice{}
			x_d.Surface = append([]int{}, Dices[x].Surface...)
			for y:=x+1; y<n; y++{
				for i:=0; i<=2; i++{
					for j:=0; j<=2; j++{
						for _, d := range direction_order{
							for _, r := range roll_order{
								y_d := Dice{}
								y_d.Surface = append([]int{}, Dices[y].Surface...)
								y_d.Move(d, i)
								y_d.Roll(r, j)
								if y_d.IsEqual(x_d){
									ans = false
									break CHECK
								}
							}
						}
					}
				}
		
			}
		}
	if ans{
		fmt.Println("Yes")
	}else{
		fmt.Println("No")
	}
}

func getIndex(ns []int, key int)(id int){
	for idx, v := range ns{
		if v==key{
			id = idx
			break
		}
	}
	return
}