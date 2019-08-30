using System;
using System.Linq;
using System.Collections.Generic;

public class Program{
    public static int[,] tatami;
    public static void Main(){
        var tate = 4;
        var yoko = 7;
        //番兵法による外周
        //0のときまだ未踏、-1のとき壁 あとは同じ畳のIDをつけていく
        tatami = new int[tate+2, yoko+2];
        for(int i=0; i<tatami.GetLength(0); i++){
            for(int j=0; j<tatami.GetLength(1); j++){
                if(i==0 || j== 0 || i==tatami.GetLength(0)-1 || j==tatami.GetLength(1)-1) tatami[i, j] = -1;
            }
        }
        try{
            setTatami(1, 1, 1);
        }catch(Exception e){
            Console.WriteLine("死");
        }
    }
    
    public static void setTatami(int h, int w, int id){
        //終了条件 最終行までいけば終わり
        //Console.WriteLine($"h:{h}, w:{w}");
        if(h>tatami.GetLength(0)-2) PrintTatami();
        else if(w>=tatami.GetLength(1)-1){
            //最終列の場合は次の列へ
            setTatami(h+1, 1, id);
        }else if(tatami[h, w]>0){
            //既に現在のマスにidがあればひとつ右に移動
            setTatami(h, w+1, id);
        }else{
            //現在のみているマスの左上と左、左上と上が同じ場合はセットできるらしい
            //（順に、左側には縦に畳が入っている・上には横に畳が入っている）
            if(tatami[h-1, w-1]==tatami[h, w-1] || tatami[h-1, w-1]==tatami[h-1, w]){
                //横にセットしていく
                if(tatami[h, w+1]==0){
                    tatami[h, w] = tatami[h, w+1] = id;
                    setTatami(h, w+2, id+1);
                    //再帰から帰ってきたらidをもとにもどす
                    tatami[h, w] = tatami[h, w+1] = 0;
                }
                //縦にセットしていく
                if(tatami[h+1, w]==0){
                    tatami[h, w] = tatami[h+1, w] = id;
                    setTatami(h, w+1, id+1);
                    //再帰から略
                    tatami[h, w] = tatami[h+1, w] = 0;
                }
            }
        }
    }
    
    public static void PrintTatami(){
        for(int i=0; i<tatami.GetLength(0); i++){
            var str = "";
            for(int j=0; j<tatami.GetLength(1); j++){
                if(i==0 || j==0 || i==tatami.GetLength(0)-1 || j==tatami.GetLength(1)-1) continue;
                if(tatami[i, j]==-1) continue;
                if(tatami[i, j]==tatami[i, j+1] || tatami[i,j]==tatami[i, j-1]) str+="-";
                if(tatami[i, j]==tatami[i+1, j] || tatami[i,j]==tatami[i-1, j]) str+="|";
                
            }
            Console.WriteLine(str);
        }
    }
}
