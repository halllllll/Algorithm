## 問題名
Counting Characters
## キーワード
連想配列

## 概要
アルファベット文字列（空白や記号含む）が入力されるから各アルファベットが何回出てきたか順番に出力する。0含む。

## 方針と読解

アルファベットはruneを利用すればa~zまで作り出せる。大文字は使わないので`strings.ToLower()`する。

goで書いててハマったのだが、グローバルに`var alphabetmap map[string]int`としてそのままmap[key]=valueと代入しようとしたら
```
panic: assignment to entry in nil map
```
などと言われた。調べると、goではmapは宣言時に自動で初期化はされないらしい。なのでmainで再度
```
alphabetmap = map[string]int{}
```
などとして初期化せねばならない。罠。

mapで扱えばいいです。 

あと、空白があったのを見逃しててなんか珍しいエラーでWAした。

## 参考
[【Go言語】assignment to entry in nil map](http://otiai10.hatenablog.com/entry/2014/08/09/154256)

[Goでアルファベットの文字列](http://or3.hatenablog.com/entry/2018/03/29/212245)

## 所感
罠。