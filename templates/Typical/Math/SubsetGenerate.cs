using System;
using System.Collections.Generic;
using System.Linq;

/*
ビットシフトによる部分集合の生成をやるだけ
*/

public class Program{
    public static void Main(){
        var collection = new string[]{"マーゲイ", "かばん", "サーバル", "トキ", "コウテイ", "タイリクオオカミ", "ヒグマ", "フェネック"};    
        var n = collection.Count();
        var lis = new List<List<int>>();
        //1を左にN個移動させている → 値を2^N倍（この場合は1の2^8倍＝256倍）している
        for(int b=0; b<(1<<n); b++){
            var arr = new List<int>();
            for(int i=0; i<n; i++){
                if((b&(1<<i))>0) arr.Add(i);
            }
            if(arr.Count()>0)lis.Add(arr);
        }
        Console.WriteLine("すべての部分集合");
        foreach(var l in lis.Select((Val, Idx)=>new{Val, Idx})){
            Console.WriteLine($"{l.Idx}番目");
            foreach(var a in l.Val){
                Console.Write($"{collection[a]} ");
            }
            Console.WriteLine();
        }
    }
}
