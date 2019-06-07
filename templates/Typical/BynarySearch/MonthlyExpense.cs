using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;

class Program{
    static int N;
    static int M;
    static int[] Expensies;
    static void Main(){
        TextReader reader;
        string filename = "";
        if(filename.Length!=0) reader = new StreamReader(filename);
        else reader = Console.In;
        var input = reader.ReadLine().Split();
        N = int.Parse(input[0]);
        M = int.Parse(input[1]);
        Expensies = new int[N];
        for(int i=0; i<N; i++){
            Expensies[i] = int.Parse(reader.ReadLine());
        }

        //最小値と最大値を初期化
        int lb = 0, ub = Int32.MaxValue;
        //絶対誤差が1以下になるまで続ける
        while(ub-lb>1){
            var mid = (lb+ub)/2;
            Console.WriteLine($"mid={mid}で試してみるよ");
            if(Check(mid)) ub = mid;
            else lb = mid;
            Console.WriteLine("次いってみよ");
        }
        Console.WriteLine("おわったよ");
        Console.WriteLine($"ub={ub}, lb={lb}");

    }
    
    static bool Check(int sum){
        int m_cnt = 1, subtotal = 0;
        foreach(var e in Expensies){
            if(sum<e){
                //そもそもsumがExpencies[i]を下回る場合は無理
                return false;
            }else if(subtotal+e<=sum){
                //現在の小計に現在の出費を足しても設定値sumを上回らないかぎり足す
                subtotal += e;
            }else{
                //それ以外、現在の小計に現在の出費を足すと設定値sumを超える場合
                //現在の小計に現在の出費をたさずに更新するだけにする。
                //こうすることで次のループは現在の出費を足した状態からスタートさせる
                //ついでに区画もインクリメントする m区画目で
                subtotal = e;
                m_cnt++;
            }
        }
        //すべてのループを終えたあと区画をどれだけ使ったか比較
        //すべての区画（の数）を使い切ってない場合・または丁度使い切っている場合はまだ設定値sumを増やせる→true
        //すべての区画（の数）を越えていると設定値sumを減らさないといけない→false
        return m_cnt<=M; 
    }
}
