using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;

public class Program{
    public static int N = 3;
    public static int[] STEPS = new int[]{0, 1, 0, -1, 0};
    public static void Main(){

        var Board = new int[N, N];
        for(int i=0; i<N; i++){
            var line = Console.ReadLine().Split().Select(int.Parse).ToArray();
            for(int j=0; j<N; j++){
                Board[i, j] = line[j];
            }
        }
        
        var Goal = new int[,]{ {1, 2, 3}, {4, 5, 6}, {7, 8, 0} };
        var queue = new Queue<State>();
        var all_list = new HashSet<long>();
        var all_dict = new Dictionary<long, int>();
        
        //スタートからゴールへ向かう経路は正値、逆は負値とする
        //処理の関係上どちらも1ステップ終えた状態から始めるとし、探索終了の際に-2をして帳尻を合わせる
        queue.Enqueue(new State{table = Goal, cnt = -1});
        queue.Enqueue(new State{table = Board, cnt = 1});
        all_dict[Board2Long(Goal)] = -1;
        all_dict[Board2Long(Board)] = 1;

        while(queue.Count()>0){
            var curr = queue.Dequeue();
            var longed = Board2Long(curr.table);
            if(all_list.Contains(longed)){
                //既に通ったパスが存在する場合、向きが異なっていれば互いに鉢合ったことになるので終了
                //つまり一方が正で他方が負である場合のみ（ほかにスマートな実装方法はないものか）
                if( (all_dict[longed]<0 && 0<curr.cnt) || curr.cnt<0 && 0<(all_dict[longed]) ){
                    var other = Math.Abs(all_dict[longed]);
                    var me = Math.Abs(curr.cnt);
                    Console.WriteLine(other+me-2);
                    break;
                }else{
                    continue;
                }
            }
            
            all_list.Add(longed);
            all_dict[longed] = curr.cnt;
            
            var Now = curr.GetPos();
            var cx = Now.X;
            var cy = Now.Y;
            for(int i=0; i<4; i++){
                var nx = cx+STEPS[i+1]; 
                var ny = cy+STEPS[i];
                if(0<=nx && nx<Board.GetLength(1) && 0<=ny && ny<Board.GetLength(0)){
                    var Nex = new Pos{Y = ny, X = nx};
                    var NexMap = curr.Swap(Nex, Now);
                    queue.Enqueue(NexMap);
                }
            }
        }
    }

    public static long Board2Long(int[,] board){
        var keta = board.GetLength(0)*board.GetLength(1)-1;
        long ret = 0;
        for(int i=0; i<board.GetLength(0); i++){
            for(int j=0; j<board.GetLength(1); j++){
                ret+=board[i,j]*(int)Math.Pow(10, keta-(i*board.GetLength(0)+j));
            }
        }
        return ret;
    }
}

public struct Pos{
    public int X{set; get;}
    public int Y{set; get;}
}

public struct State{
    public int cnt{set; get;}
    public int[,] table{set; get;}
    public Pos GetPos(){
        var retPos = new Pos{X = -1, Y = -1};
        for(int i=0; i<this.table.GetLength(0); i++){
            for(int j=0; j<this.table.GetLength(1); j++){
                if(this.table[i, j]==0){
                    retPos.X = j;
                    retPos.Y = i;
                }
            }
        }
        return retPos;
    }

    public State Swap(Pos pre, Pos nex){
        var _tmp = this.table.Clone() as int[,];
        var _cnt = this.cnt;
        var ad = _cnt>0 ? 1 : -1;
        _tmp[nex.Y, nex.X] = this.table[pre.Y, pre.X];
        _tmp[pre.Y, pre.X] = this.table[nex.Y, nex.X];
        return new State{cnt = _cnt+=ad, table = _tmp};
    }
}
