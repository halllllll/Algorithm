using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;
using static ExClass.ExtendClass;

/*
DFSによる組み合わせ順列の生成
実際最初にインデックスの組み合わせを作ってしまえば各要素（==index）をインクリメント%lengthで
Countぶん回せばすべてのインデックスの組み合わせは出せるので、
二回目以降の判定は不必要になるので、もっと早くできそう
*/

public class Hello{
    public static void Main(){
        //出力設定
        var sw = new StreamWriter(Console.OpenStandardOutput()){AutoFlush = false};
        Console.SetOut(sw);
        //深さ優先探索でやってみる
        
        var numbers = Console.ReadLine().Split().ToArray();
        var result = numbers.Permutation();
        foreach(var r in result){
            Print(r);
        }
        Console.Out.Flush();
    }
    
    //コレクション出力するマン
    public static void Print<T>(IEnumerable<T> someArray){
        var ans = string.Join(",", someArray);
        Console.WriteLine(ans);
    }
}
