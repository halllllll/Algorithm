## 問題名
Finding A Word
## キーワード
標準入力?, 文字列比較
## 概要
Tに含まれる単語Wの数を答える。単語とはスペースか改行で囲まれた独立した文字列のことである。なお、Tは複数行に分かれており、最後の行は`END_OF_TEXT`である。なお、大文字小文字は区別しない
## 方針と読解
入力数が規定されていないので、入力できなくなるか`END_OF_TEXT`が入力されるまで入力し続ける。<br>
単語なので一行ごとに読み込んでそのまま処理したり、一単語の中で`find`などするのは間違い（最初これ気付かずに5回ほどWAした）。ふつうに`==`などでwと比較する。<br>
なお、大文字小文字の区別がないからといって入力即`ToUpper`などで合わせようとすると`end_of_text`が入力されて比較してしまいまだ余地があるのにループを終了してしまうという罠がある
## 参考
goでやった。単語ごとなので`fmt.Scan()`で都合がいいのだが`Scanner`を使った。
```go
scanner := bufio.NewScanner(os.Stdin)
scanner.Split(bufio.ScanWords)
var t, w string
scanner.Scan()
w = strings.ToLower(scanner.Text())
```

## 所感
あっはい