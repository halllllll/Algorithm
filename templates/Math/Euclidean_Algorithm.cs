/*
ユークリッドの互除法で細大公約数を求めるやつの拡張メソッドを書いてみる
*/
using System;
using System.Linq;
using System.Collections.Generic;

class Program{
    static void Main(){
        var num1 = 28937;
        var num2 = 29127;
       //拡張メソッドを使っているのでIntegerクラスの静的メソッドのように使える.
       Console.WriteLine($"拡張メソッドversion Num.Gcd(Num2) のように使う");
       var ans = num1.Gcd(num2);
       Console.WriteLine(ans);
       //格調メソッドを使わないバージョン
       Console.WriteLine($"ふつうの静的メソッドで書く Gcd(Num, Num2) のように使う");
       var ans2 = Gcd(num1, num2);
       Console.WriteLine(ans2);

       //実際は静的メソッドとしてクラスにアクセスしても使える
       Console.WriteLine($"実際は静的メソッドとしてクラスにアクセスしても使える Class.Gcd(Num, Num2) のように使う");
       Console.WriteLine(ExtendClass.Gcd(num1, num2));
    }

    //ふつうのメソッド
    public static int Gcd(int x, int y){
        if(x<y){
            return Gcd(y, x);
        }
        while(y!=0){
            var tmp = x%y;
            x = y;
            y = tmp;
        }
        return x;
    }
}

//格調メソッドは静的クラス内に静的メソッドとして定義する
static class ExtendClass{
    //GreatestCommonDevisor
    public static int Gcd(this int x, int y){
       if(x<y){
           return Gcd(y, x);
       }
       while(y!=0){
           var tmp = x%y;
           x = y;
           y = tmp;
       }
       return x;
  }
}
