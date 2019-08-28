package main
import (
	"fmt"
	"os"
	"bufio"
	"strconv"
)

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	for scanner.Scan(){
		input := scanner.Text()
		if input=="-"{
			break
		}
		scanner.Scan()
		m, _ := strconv.Atoi(scanner.Text())
		for i:=0; i<m; i++{
			scanner.Scan()
			h, _ := strconv.Atoi(scanner.Text())
			input = input[h:]+input[:h]
		}
		fmt.Println(input)
	}
}