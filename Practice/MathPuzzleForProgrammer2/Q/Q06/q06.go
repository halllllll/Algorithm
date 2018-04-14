package main
import (
	"fmt"
)

func main(){
	ans := 0
	for y:=2; y<=1000; y++{
		for x:=1; x<y; x++{
			ans += recursion(x, y, 0)
		}
	}
	fmt.Println(ans)
}

func recursion(w, h, boxcount int)int{
    if boxcount>20{
        // boxcountが20を超えた時点で無理
        return 0
    }
	if (w==0 || h==0){
        // 残りの縦横が存在しないのでここで精算
		if boxcount==20{
			return 1
		}else{
			return 0
		}
    }
	if (w==1 || h==1) {
        // いずれかが1だと他方の長さぶんの1x1の正方形ができる
		return recursion(0, 0, boxcount+w*h)
	}
	if w<h{
		return recursion(w, h-w, boxcount+1)
	}else if w>h{
		return recursion(w-h, h, boxcount+1)
	}else{
        // w==hの場合、残った長方形とは正方形である
		return recursion(0, 0, boxcount+1)
	}
}