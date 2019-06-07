using System;
using System.Linq;
using System.Collections.Generic;

class Program{
    static long n;
    static long[] s;
    static long q;
    static long[] t;
    static void Main(){
        n = long.Parse(Console.ReadLine());
        s = Console.ReadLine().Split().Select(long.Parse).ToArray();
        q = long.Parse(Console.ReadLine());
        t = Console.ReadLine().Split().Select(long.Parse).ToArray();
        long count = 0;
        for(int i=0; i<q; i++){
            if(Check(t[i]))count++;
        }
        Console.WriteLine(count);
    }
    
    static bool Check(long l){
        //ソート済のsに対して二分探索をしかける
        //順序としては最小値と最大値を使ってmidをとったりする
        long lb = 0, ub = n;
        while(lb<ub){
            var mid = (lb+ub)/2;
            if(s[mid]==l) return true;
            else if(l<s[mid]) ub = mid;
            else lb = mid+1;
        }
        return false;
    }
}
