using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;
/*
union-findの復習
ランク付け+経路圧縮によってアッカーマン関数の逆関数時間で解ける（よくわからんが）
*/

public class Program{
    public static int[] array;
    public static int[] rank;
    public static void Main(){
        var filename = "";
        var reader = new StreamReader(filename);
        var nq = reader.ReadLine().Split().Select(int.Parse).ToArray();
        int N = nq[0], Q = nq[1];
        array = Enumerable.Range(0, N).ToArray();
        rank = Enumerable.Repeat(1, N).ToArray();
        for(int i=0; i<Q; i++){
            var info = reader.ReadLine().Split().Select(int.Parse).ToArray();
            int query = info[0], a = info[1], b = info[2];
            if(query==0) Union(a, b);
            else{
                if(Same(a, b))Console.WriteLine("YES");
                else Console.WriteLine("NO");
            }
        }
    }

    //グループの親を返す
    public static int Find(int target){
        /*
        経路圧縮しないバージョン
        （探索時にさかのぼるそれぞれの親をグループの根に直接つなぐ。
        これによってインデックスの要素がその親を指す、というのではなくなる？）
        while(target!=array[target]){
            target = array[target];
        }
        */
        //経路圧縮するバージョン
        if(target!=array[target]){
            array[target] = Find(array[target]);
        }
        return array[target];
    }

    //グループの親が異なっていればbのグループの親をaにつなげる
    public static void Union(int a, int b){
        var parent_a = Find(a);
        var parent_b = Find(b);
        if(parent_a!=parent_b){
            //木の高さの低い方を高い方につなげる。
            //このようにすると木の高さの上限は変わらず平坦化される
            if(rank[parent_a]<rank[parent_b]){
                array[parent_a] = parent_b;
            }else{
                array[parent_b] = parent_a;
                //低いほうの高さを更新
                rank[parent_a]++;
            }
        }
    }

    //親が同じかどうかの判定
    public static bool Same(int a, int b){
        if(Find(a)!=Find(b))return false;
        return true;
    }
}
