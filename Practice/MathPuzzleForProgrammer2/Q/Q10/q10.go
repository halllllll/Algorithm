package main

import (
	"fmt"
	"math"
)

var pref = []int{5381773, 1308265, 1279594, 2333899, 1023119, 1123891, 1914039, 2916976, 1974255, 1973115, 7266534, 6222666, 13515271, 9126214, 2304264, 1066328, 1154008, 786740, 834930, 2098804, 2031903, 3700305, 7483128, 1815865, 1412916, 2610353, 8839469, 5534800, 1364316, 963579, 573441, 694352, 1921525, 2843990, 1404729, 755733, 976263, 1385262, 728276, 5101556, 832832, 1377187, 1786170, 1166338, 1104069, 1648177, 1433566}
var max_seat = 289

func main() {
	left, right := 0, math.MaxInt64
	for left < right {
		mid := int(math.Floor((float64(left) + float64(right)) / 2.0))
		seat := 0
		for _, v := range pref {
			seat += int(math.Ceil(float64(v) / float64(mid)))
		}
		if seat == max_seat {
			for _, v := range pref {
				fmt.Println(v / mid)
			}
			break
		}
		if seat < max_seat {
			// 席が少なすぎるので大きくなる方にシフト
			right = mid
		} else {
			// 席が多すぎるので小さくなる方にシフト
			left = mid + 1
		}
		/*
			if seat > max_seat {
				// 席が多すぎるので小さくなる方にシフト
				left = mid + 1
			} else {
				// 席が少なすぎるので大きくなる方にシフト
				right = mid
			}
		*/
	}
}
