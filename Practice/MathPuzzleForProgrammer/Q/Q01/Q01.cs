using System;
using System.Linq; 
using System.Collections.Generic;

public class Program{
    public static void Main(){
        int n = 10;
        while(true){
            var bin = Convert.ToString(n, 2);
            var Rebin = new string(bin.Reverse().ToArray());
            var oct = Convert.ToString(n, 8);
            var Reoct = new string(oct.Reverse().ToArray());
            var Ren = new string(n.ToString().Reverse().ToArray());
            if(n.ToString() == Ren && bin == Rebin && oct == Reoct) break;
            n++;
        }
        Console.WriteLine(n);
    }
}
