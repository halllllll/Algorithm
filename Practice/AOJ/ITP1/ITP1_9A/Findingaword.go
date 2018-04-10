package main
import (
	"os"
	"fmt"
	"strings"
	"bufio"
)

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	var t, w string
	scanner.Scan()
	w = strings.ToLower(scanner.Text())
	cnt := 0
	for scanner.Scan(){
		t = scanner.Text()
		if t=="END_OF_TEXT"{
			fmt.Println(cnt)
		}
		if strings.ToLower(t)==w{
			cnt++
		}
	}
}