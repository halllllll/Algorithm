public class BFS{
    public string EndMark { get; set; } = "終";
    public string OKMark { get; set; } = ".";
    public string NGMark { get; set; } = "#";
    public string[,] Map {get; set;}
    public string[] mapdata { get; set; }
    public Pos Start { get; set; }
    public Pos Goal {get; set; }
    public int Height;
    public int Width;
    public HashSet<Pos> Path;
    public BFS(string[] _data, Pos _start, Pos _goal){
        this.mapdata = _data;
        this.Start = _start;
        this.Goal = _goal;
        this.Path = new HashSet<Pos>();
        initMap();
    }

    //地図データ（文字列の配列として）、スタートとゴールのPosから地図を初期化
    public void initMap(){
        this.Height = mapdata.Length;
        this.Width = mapdata[0].Count();
        this.Map = new string[Height, Width];
        for(int i=0; i<Height; i++){
            var line = mapdata[i];
            for(int j=0; j<Width; j++){
                this.Map[i, j] = line[j].ToString();
            }
        }
        //マスにはそこまでにかかるステップ数を記録するんだって
        Map[Start.Y, Start.X] = "0";
        Map[Goal.Y, Goal.X] = EndMark;
    }

    //プリントするよ
    public void Print(){
        for(int i=0; i<Height; i++){
            for(int j=0; j<Width; j++){
                Console.Write($"{Map[i, j]} ");
            }
            Console.WriteLine();
        }        
    }

    //探索するよ
    public int Search(){
        //キューを用意
        var queue = new Queue<Pos>();
        //キューにスタート位置を追加
        queue.Enqueue(new Pos{
            X = Start.X,
            Y = Start.Y,
        });
        //既に通ったことのあるグリッドを保存するやつもスタート位置を更新しておくよ
        this.Path.Add(this.Start);
        while(queue.Count()>0){
            var curr = queue.Dequeue();
            //Print();
            if(isGoaled(curr)){
                //ゴールは「次のステップ」なのでゴールするにはもう1ステップ必要だよ
                //Console.WriteLine("Congulatulation");
                var ans = Convert.ToInt32(Map[curr.Y, curr.X])+1;
                Print();
                return ans;
            }
            //進めるところのうちでまだ通っていないマスをキューに追加するよ
            foreach (var nex in Step(curr))
            {
                queue.Enqueue(nex);
                //一度通ったところはもう通らないように覚えておこうね
                Path.Add(nex);
                //マップを更新するんだ
                updateMap(nex, curr);
            }
        }
        //探索失敗したら-1なんだ
        //Console.WriteLine("にゃーん");
        return -1;
    }

    public void updateMap(Pos nexP, Pos preP){
        var nexCnt = Convert.ToInt32(Map[preP.Y, preP.X])+1;
        Map[nexP.Y, nexP.X] =  nexCnt.ToString();
    }

    //四方のうちで進めるところを返すよ
    //進めるマークがついていてまだ未踏の場所のことだね
    public IEnumerable<Pos> Step(Pos pos){
        return AroundGrid(pos).Where(p=>new string[]{OKMark, EndMark}.Contains(Map[p.Y, p.X])).Where(p=>!Path.Contains(p)).ToArray();
    }

    //今の座標を受け取って次のステップの候補地を出すよ　ただの四方抽出だね
    public IEnumerable<Pos> AroundGrid(Pos p){
        //地図からはみ出さない限りは探索できるよ
        var around = new int[]{0, 1, 0, -1, 0}; //ここにわざわざ書く意味はないね
        for(int i=0; i<around.Length-1; i++){
            var nx = p.X+around[i+1];
            var ny = p.Y+around[i];
            if(0<=nx && nx<Width && 0<=ny && ny<Height){
                yield return new Pos{X = nx, Y = ny};
            }
        }
    }

    //次のステップでゴールになるか判断するよ
    public bool isGoaled(Pos pos){
        var ans = AroundGrid(pos).Any(p=>Map[p.Y, p.X] == EndMark);
        return ans;
    }
}

//座標情報を表す構造体だよ
public struct Pos{
    public int X { get; set; }
    public int Y { get; set; }
}
