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

func (d *Dice)Roll(dir string){
	switch dir{
	case "R":
		d.Surface[3], d.Surface[1], d.Surface[2], d.Surface[4] = d.Surface[1], d.Surface[2], d.Surface[4], d.Surface[3]
	case "L":
		d.Surface[3], d.Surface[1], d.Surface[2], d.Surface[4] = d.Surface[4], d.Surface[3], d.Surface[1], d.Surface[2]
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
	var n int
	fmt.Scan(&n)
	for i:=0; i<n; i++{
		var up, front int
		fmt.Scan(&up, &front)
		u := getIndex(d.Surface, up)
		switch u{
			case 0:
				// 何もしなくていい
				break
			case 1:
				d.Move("N")
			case 2:
				d.Move("W")
			case 3:
				d.Move("E")
			case 4:
				d.Move("S")
			default:
				// 適当に2回同じ方向に回す
				d.Move("N")
				d.Move("N")
		}
		// d.GetStatus()
		f := getIndex(d.Surface, front)
			switch f{
				//4通りしかないはず
			case 3:
				d.Roll("L")
			case 1:
				break
			case 2:
				d.Roll("R")
			case 4:
				// 適当に同じ方向に2回回す
				d.Roll("R")
				d.Roll("R")
			default:
				fmt.Println("fuckkkkkkkkk")
		}
		// d.GetStatus()
		fmt.Println(d.Surface[2])
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