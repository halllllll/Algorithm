namespace ExClass
{
    using System.Linq;
    using System.Collections.Generic;
    
    public static class ExtendClass{
        public static IEnumerable<List<T>> Permutation<T>(this T[] target){
            //ほんとは再帰したかったんだけどぜんぜんやり方わからなかったのでおとなしくスタックにした
            //そのついでに外部ファイルにして拡張メソッドで呼び出すようにした
            //探索では要素は必要とせず、インデックスのみ取り扱いたい
            //したがってジェネリック版だがインデックスだけを見れば良い
            foreach(var n in target.Select((Val, Idx)=>new{Val, Idx}).Select(n=>n.Idx)){
                var stack = new Stack<List<int>>();
                //nのみを要素にもつように初期化
                var initarray = new List<int>();
                initarray.Add(n);
                stack.Push(initarray);
                //で　ここからが探索開始
                while(stack.Count()>0){
                    //スタックから現在の配列を取り出す
                    var nowarray = stack.Pop();
                    //終了条件 それ以外は継続
                    if(nowarray.Count()==target.Count()){
                        //基準となるtargetにインデックスを合わせてやる
                        //ジェネリックがその機能を発揮するのはここ
                        var output = new List<T>();
                        foreach(var i in nowarray){
                            output.Add(target[i]);
                        }
                        yield return output;
                    }
                    //次に追加できるやつはすべて詰め込む
                    //追加する要素はインデックス
                    for(int nexidx = 0; nexidx<target.Count(); nexidx++){
                        //現在の配列にまだインデックスが含まれていない場合は詰め込む
                        if(!nowarray.Contains(nexidx)){
                            var nexarray = new List<int>(nowarray);
                            nexarray.Add(nexidx);
                            stack.Push(nexarray);
                        }
                    }
                }
            }
        }
    }
}
