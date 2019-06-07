/*
ρ法で素因数分解を試みる
実装はwikipediaを参考にしてみる
*/

using System;
using System.Linq;
using System.Collections.Generic;
using System.Diagnostics;

class Program{
    static void Main(){
        //ulong n = 2817941917120100129;    無理
        ulong n = 2817941917120100000;      //余裕
        Console.WriteLine($"{n}をρ法で素因数分解してみます");
        var watch = new Stopwatch();
        watch.Start();
        
        var ans = n.PrimeFactorDecomposition();
        //OrderByでulongを使えないっぽい。
        //自作したりオーバーロードしたりするのしんどい≒自作できない、のでstringに変換して文字列の長さを加えて匿名型でやることにした
        var outputs = ans.Select(c=> new { k=(c.Key).ToString(), v=(c.Value).ToString(), length=(c.Key).ToString().Count() }).OrderBy(o=>o.length).ThenBy(t=>t.k).ToArray();
        var nature_outputs = outputs.Select(s=>$"{s.k}^{s.v}").ToArray();
        var output = String.Join(" * ", nature_outputs);
        Console.WriteLine(output);
        /*
        var ans2 = n.Factoring();
        ある約数だけを得たいならこっちでもいい
        Console.WriteLine(ans2);
        */
        Console.WriteLine($"実行時間 {watch.ElapsedMilliseconds}ミリ秒");
    }
}


static class ExtendClass{
    static ulong target;
    static ulong seed;
    public static Dictionary<ulong, ulong> PrimeFactorDecomposition(this ulong x){
        var tmp = x;
        var dict = new Dictionary<ulong, ulong>();
        if(tmp.IsPrime()){
            dict[tmp] = 1;
            return dict;
        }
        ulong ret;
        while(tmp/(ret=tmp.Factoring())!=0){
            if(dict.ContainsKey(ret))dict[ret]++;
            else dict[ret]=1;
            tmp/=ret;
            //Console.WriteLine($"tmp={tmp}");
            if(tmp==1)break;
        }
        return dict;
    }

    //べつに外部から呼び出さないのでprivateでもいいが
    public static ulong Factoring(this ulong n, ulong _seed=3){
        if(n.IsPrime())return n;
        ulong x = 2, y = 2, d = 1;
        target = n;
        seed = _seed;
        //Console.WriteLine($"target={target}, seed={seed}");
        while(d==1){
            x = f(x);
            y = f(f(y));
            var dif = x>y ? x-y : y-x;
            d = gcd(dif, target);
            seed++;         //これが無限ループを避けるポイント？どういう値がいいorダメなんだろ
            //Console.WriteLine($"d={d}, seed={seed}");
        }
        seed = 0;
        //2で割り切るところを実装しないとなんか駄目
        if(d%2==0)return 2;
        if(!d.IsPrime())return d.Factoring(seed+1);
        return d.Factoring(1);
    }
    //nを法とする、擬似乱数発生関数
    private static ulong f(ulong n){
        //cは0,-2以外のなんかでいいらしい
        var ret = (ulong)Math.Pow(n, 2) + seed;
        return ret%target;
    }

    //素数判定
    private static bool IsPrime(this ulong n){
        if(n<2)return false;
        for(ulong m=2; m<=(ulong)Math.Sqrt(n); m++){
            if(n%m==0)return false;
        }
        return true;
    }

    //二数の最大公約数を返す（ユークリッドの互除法）
    private static ulong gcd(ulong a, ulong b){
        if(a<b) return gcd(b, a);
         while(b!=0){
            var tmp = a%b;
            a = b;
            b = tmp;
         }
         return a;
    }
}
