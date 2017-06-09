//http://poj.org/problem?id=2456のやつ
using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;

class Program{
    static int[] distances;
    static int N;
    static int M;
    static void Main(){
        TextReader reader;
        string filename = "";
        filename = @"";
        if(filename.Length!=0)reader = new StreamReader(filename);
        else reader = Console.In;
        
        //ほんとは制約的にはintでなくlongが正しそう
        var nm = reader.ReadLine().Split();
        N = int.Parse(nm[0]);
        M = int.Parse(nm[1]);
        distances = new int[N];
        for(int i=0; i<N; i++){
            distances[i] = int.Parse(reader.ReadLine());
        }
        /*
        距離pを与えたときに、その距離をとればすべての牛が牛舎におさまるかどうかを判定するbool値を返すメソッドを用意する。
        
        ただし今回の場合、牛舎の位置はソートされているとは限らないので先にソートしておく。

        たとえば、10という距離を最初にとったとして、すべての牛が牛車に収まりきらなかった場合、その距離は長すぎることになるので短くする。すべての牛が収まった場合も、その距離より短くても収まるかもしれないので短くする。

        この操作を繰り返せば最適解が見つかる。
        */
        distances = distances.OrderBy(o=>o).ToArray();

        //最大値と最小値を用意
        int ub = Int32.MaxValue;
        int lb = 0;
        //条件は、絶対誤差が1になるまで（すべて整数なので）
        while(ub-lb>1){
            //中間値を出す
            var mid = (ub+lb)/2;
            //メソッドに投げる
            //trueが返る場合はすべての牛が牛舎に収まった場合
            //すなわちまだmidを短くできるかもしれない。
            //falseの場合は収まりきらなかった場合。
            //すなわち距離を縮めないとダメ
            if(Check(mid))lb = mid;
            else ub = mid;
        }
        //「最も近い二頭の牛の間の間隔を最大化しなさい」なので最小値の最大化
        //なのでlbを求めればよい
        Console.WriteLine(lb);

    }

    static bool Check(int dist){
        int pos = 0;
        //最初以外のすべての牛舎において
        for(int i=1; i<M; i++){
            //仮の次の牛舎の位置
            int nex = pos+1;
            //牛舎の末尾でないかつ「前の牛舎と次の牛舎の差がdistより狭い」間
            while(nex<N && distances[nex]-distances[pos]<dist){
                nex++;
                //もし牛舎の末尾まで（すべての牛を使い切ることなく）達してしまったら、distが広すぎたということになる
                if(nex==N)return false;
            }
            //仮の次の牛舎の位置が決まったので更新してさらに次の牛舎の位置へ
            pos = nex;
        }
        //最後まで牛車に牛が納まったらdistが狭かったかもしれないということになる
        return true;
    }
}
