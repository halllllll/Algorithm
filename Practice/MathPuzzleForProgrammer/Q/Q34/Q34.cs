using System;
using System.Linq;
using System.IO;
using System.Diagnostics;
using System.Collections.Generic;

public class Program{
    public static void Main(){
        var stream = new StreamWriter(Console.OpenStandardOutput()){AutoFlush=false};
        var watch = new Stopwatch();
        watch.Start();
        Console.SetOut(stream);
        //盤面が縦横9マスなので飛車角それぞれについてやるのでO(9^4)
        var Board = new int[9, 9];
        var cnt = 0;
        var hsteps = new int[]{0, 1, 0, -1, 0};
        var ksteps = new int[]{-1, 1, 1, -1, -1};
        for(int hi=0; hi<9; hi++){
            for(int hj=0; hj<9; hj++){
                var tmp = 0;
                for(int ki=0; ki<9; ki++){
                    for(int kj=0; kj<9; kj++){
                        if(hi==ki && hj==kj) continue;
                        Board[hi, hj] = Board[ki, kj] = 2;  //べつに1でもいい　そんときはcntに足すときに飛車角がそれぞれ占領しているぶん2を引く
                        //飛車の軌道上に角がいないか。いたらそこまでは動ける 逆も同じように
                        //めんどくさいのでひとつのループ内でやってしまえ
                        //最も計算量が多くなるのは駒が中央にあるときだが、せいぜい4*4*2程度で低数倍で無視できる
                        for(int p=0; p<4; p++){
                            int chi = hi+hsteps[p], chj = hj+hsteps[p+1];
                            int cki = ki+ksteps[p], ckj = kj+ksteps[p+1];
                            while( (0<=chi&&chi<9&&0<=chj&&chj<9) ){
                                if(chi==ki&&chj==kj) break;
                                if(Board[chi, chj]==0)Board[chi, chj]=1;
                                chi+=hsteps[p];
                                chj+=hsteps[p+1];
                            }
                            
                            while( (0<=cki&&cki<9&&0<=ckj&&ckj<9) ){
                                if(cki==hi&&ckj==hj) break;
                                if(Board[cki, ckj]==0)Board[cki, ckj]=1;
                                cki+=ksteps[p];
                                ckj+=ksteps[p+1];
                            }
                            
                        }
                        //Print(Board);
                        cnt+=Check(Board);
                        Board = new int[9, 9];
                    }
                }
            }
        }
        Console.WriteLine(cnt);
        Console.WriteLine($"実行時間 {watch.ElapsedMilliseconds}ミリ秒");
        Console.Out.Flush();
    }
    public static void Print(int[,] map){
        for(int i=0; i<map.GetLength(0); i++){
            for(int j=0; j<map.GetLength(1); j++){
                Console.Write($"{map[i,j]} ");
            }
            Console.WriteLine();
        }
        
    }
    public static int Check(int[,] map){
        var ret = 0;
        for(int i=0; i<map.GetLength(0); i++){
            for(int j=0; j<map.GetLength(1); j++){
                if(map[i,j]==1)ret++;
            }
        }
        return ret;
    }
}
