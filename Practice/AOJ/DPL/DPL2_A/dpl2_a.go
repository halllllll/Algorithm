package main
import "fmt"
var table [][]int
func main(){
    // Traveling Salesman ProblemはbitDPで解く
    var v, e int
    fmt.Scan(&v)
    fmt.Scan(&e)
    INF := 10000000000
    table = make([][]int, v)
    for i:=0; i<v; i++{
        table[i] = make([]int, v)
        for j:=0; j<v; j++{
            table[i][j] = INF
        }
    }
    for i:=0; i<e; i++{
        var s, t, d int
        fmt.Scan(&s)
        fmt.Scan(&t)
        fmt.Scan(&d)
        table[s][t] = d
        // table[t][s] = d 
    }
    
    dp := make([][]int, 1<<uint64(v))
    for i:=0; i<(1<<uint64(v)); i++{
        dp[i] = make([]int, v)
        for j:=0; j<v; j++{
            dp[i][j] = INF
        }
    }
    dp[1][0] = 0
    
    // 配るDP
    // iは訪れた場所の集合（をビットで表したもの）
    for i:=0; i<(1<<uint64(v)); i++{
        // jは直前に訪れた場所
        for j:=0; j<v; j++{
            if dp[i][j] == INF{
                continue
            }
            // kは次に訪れる場所
            for k:=0; k<v; k++{
                // なので、iのk番目のビットが立っていればすでに訪れている
                if (i>>uint64(k))%2==1{
                    continue
                }
                // k番目の場所を訪れたことにするのでビットを立てる
                next_i := i | (1<<uint64(k))
                dp[next_i][k] = min(dp[next_i][k], dp[i][j]+table[j][k])
            }
        }
    }
    
    // TSPは閉路なので、最後に「最初に訪れたところに戻るコスト」を加える
    ans := INF
    for i:=0; i<v; i++{
        if dp[(1<<uint64(v))-1][i] == INF{
            continue
        }
        ans = min(ans, dp[(1<<uint64(v))-1][i]+table[i][0])
    }
    if ans == INF{
        // 経路が存在しない サンプル2でそんなことある？かと思ったら入力で与えられるのは双方向じゃないっぽい？
        fmt.Println(-1)
    }else{
        fmt.Println(ans)
    }
}

func min(a, b int)int{
    if a < b{
        return a
    }else{
        return b
    }
}
