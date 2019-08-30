using System;
using System.Linq;
using System.Collections.Generic;
/*
AOJのDPL: Longest Increaseing Subsequence Problemより。
(http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D)
dpだけじゃ勝てなかったよ。。。。
あとなんかこれで提出しても通らないテストケースがあって、
おかしいなと思いつつDPだけで回してみたやつは答えは合ってた（当然間に合わないけど）
なのでほとんど参考にならんけど一応
*/

public class Program{
    public static int N;
    public static int[] A;
    public static void Main(){
        N = int.Parse(Console.ReadLine());
        A = new int[N];
        for(int i=0; i<N; i++){
            A[i] = int.Parse(Console.ReadLine());
        }
        //最長増加部分列問題を動的計画法とバイナリサーチで解く
        var L = Enumerable.Repeat(int.MaxValue, N).ToArray();
        int length = 1;
        L[0] = A[0];
        for(int i=1; i<N; i++){
            if(L[length-1]<A[i]){
                L[length] = A[i];
                length++;
            }else{
                //A[i]をLの適切な場所に入れて置き換える。
                //適切な場所とは、LのうちでA[i]を下回る最大の数値のあるインデックスである。
                var alterIdx = LowerBound(L, A[i]);
                L[alterIdx] = A[i];
            }
        }
        Console.WriteLine(length);
    }
    
    //arrayのうちでtargetを下回る最大の値のインデックスを返す
    public static int LowerBound(int[] array, int target){
        int left = 0;
        int right = array.Count();
        int mid = 0;
        while(left<right){
            mid = (right+left)/2;
            if(array[mid]==target) break;
            if(target<array[mid])right = mid;
            else left = mid+1;
        }
        return left;
    }
}
