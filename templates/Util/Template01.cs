using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Diagnostics;
using System.Text;

public class Program{
    public static void Main(){
        var watch = new Stopwatch();
        watch.Start();
        var isTest = true;
        var stream = new StreamWriter(Console.OpenStandardOutput()){AutoFlush = false};
        Console.SetOut(stream);
        TextReader reader;
        string filename="";
        filename=@"";
        if(filename.Length!=0){
            reader = new StreamReader(filename);
        }else{
            reader = Console.In;
        }


        watch.Stop();
        if(isTest){
            Console.WriteLine($"実行時間{watch.ElapsedMilliseconds}ミリ秒");
        }
        Console.Out.Flush();
    }
}
