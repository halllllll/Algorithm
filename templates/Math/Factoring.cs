/*
素因数分解するだけです
愚直にデクリメントして約数がみつかったら割れるだけ割る、みたいな感じ
*/
using System;
using System.Linq;
using System.Collections.Generic;

public class Program{
    public static void Main(){
        var num = 8937234;
        Console.WriteLine($"{num}を素因数分解するお(´・ω・｀)");
        Console.WriteLine(Factoring(num));
    }

    public static string Factoring(long n){
        var m = n;
        var dict = new Dictionary<long, long>();
        while(n!=1){
            m--;
            if(n%m==0){
                var d = n/m;
                while(n%d==0){
                    if(!(dict.ContainsKey(d)))dict[d]=1;
                    else dict[d]++;
                    n/=d;
                }
            m=n;
            }
        }
        var factors = dict.Select(content=>$"{content.Key}^{content.Value}").ToArray();
        var results = String.Join(" * ", factors);
        return results;
    }
}
