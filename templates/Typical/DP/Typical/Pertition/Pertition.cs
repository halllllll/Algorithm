using System;
using System.Linq;
using System.Collections.Generic;

public class Program{
    public static void Main(){
        //分割数問題
        //n個のものをm個以下に分割するときの分割の仕方の総数
        var n = 4;
        var m = 3;
        var dp = new int[m+1, n+1];
        //初期化 i=1のとき dp[i, j] = 1
        for(int i=0; i<m+1; i++) dp[1, 0] = 1;
        dp[0, 0] = 1;
        for(int i=1; i<m+1; i++){
            for(int j=0; j<n+1; j++){
                if(j<i) dp[i, j] = dp[i-1, j];
                else dp[i, j] = dp[i-1, j]+dp[i, j-i];
            }
        }
        Print(dp);
        Console.WriteLine($"answer: {dp[m,n]}");
    }
    public static void Print(int[,] table){
        for(int i=0; i<table.GetLength(0); i++){
            for(int j=0; j<table.GetLength(1); j++){
                Console.Write($"{table[i, j]} ");
            }
            Console.WriteLine();
        }
    }
}
