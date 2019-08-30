package main
import "fmt"

func main(){
	var n int
	fmt.Scan(&n)
	// math使うのすらめんどくさい そもそもnは整数値なので
	fmt.Println(n*n*n)
}
