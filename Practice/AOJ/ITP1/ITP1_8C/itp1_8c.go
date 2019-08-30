package main
import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

func craetea2z() string {
	alphabet := make([]rune, 0)
	for cur := []rune("a"); ; cur[0] += 1 {
		alphabet = append(alphabet, cur[0])
		if string(cur[0]) == "z" {
			break
		}
	}
	return string(alphabet)
}

var alphabetmap map[string]int

func main() {
	alphabetmap = map[string]int{}
	alphabet := craetea2z()
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	for scanner.Scan(){
		s := strings.ToLower(scanner.Text())
		for _, v := range []rune(s){
			if _, ok := alphabetmap[string(v)]; ok{
				alphabetmap[string(v)]+=1
			}else{
				//fmt.Println(string(v))
				alphabetmap[string(v)]=1
			}
		}
	}
	for _, v := range []rune(alphabet){
		fmt.Printf("%s : %d\n", string(v), alphabetmap[string(v)])
	}
}