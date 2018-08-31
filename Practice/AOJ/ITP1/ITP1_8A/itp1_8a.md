## 問題名
Toggling Cases
## キーワード
文字列操作, 置換
## 概要
文字列が与えられる。大文字なら小文字、小文字なら大文字に直す。
## 方針と読解
入力される文字列が大文字か小文字かで処理が分かれる。一様に`upper`なり`upcase`なりを呼べばいいというものではない。

1文字ずつ調べて変換する方法が一番楽。ただし大体の言語にはupcaseとかlowcaseはあると思うが、isupcaseとかislowcaseとなるとわからない。

置換する方法は大体の言語ならStringのreplaceとか、正規表現のsubとかそういうのがあるはず。

また、アルファベットをA-Zのリストで取得したい場合は、コードポイントから変換する方法がどの言語でもありそうなので使いやすそう。以下はpythonで書いてみたやつ。
```python
>>> [chr(c) for c in range(65, 65+24)]
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
```

あるいは、アルファベット程度ならば対応するテーブルを作ってしまうという手もある。

### python
python便利。アルファベットの対応表を作るためアルファベットをaからZまでほしかったので調べたらstringから`ascii_lowercase`とかあるらしい。対応表の作成は辞書にして`maketrans`、置換は`str.translate`で一発でいける。
```python
from string import ascii_lowercase, ascii_uppercase
s = input()
table = str.maketrans(dict(zip(ascii_lowercase+ascii_uppercase,
                               ascii_uppercase+ascii_lowercase)))
print(s.translate(table))
```
ただまあ言語で殴った感じがあって競プロとは違う。

### Ruby
pythonの直後に解いたからすっかりrepalceするよかtableを用意する方法でええやんけ脳になってそのまま書いた。アルファベット文字列を作るのも簡単だし。
```ruby
s = gets.chomp
table = Hash[*[*'a'..'z'].zip([*'A'..'Z']).flatten]
table.merge!(table.invert)
s.each_char do |c|
    print table.key?(c) ? table[c] : c
end
puts 
```

## 参考
何気にRubyでHashって使ったことなかったのでこれ読んだ。  
[Ruby における hash 操作の逆引きまとめ](http://tech-dig.hatenablog.com/entry/2016/09/10/214426#%E7%89%B9%E5%AE%9A%E3%81%AE%E3%82%AD%E3%83%BC%E3%81%8C%E5%AD%98%E5%9C%A8%E3%81%99%E3%82%8B%E3%81%8B%E8%AA%BF%E3%81%B9%E3%82%8B)

rubyで`str.each`くらいできるだろとやったらエラー吐かれたので調べたら`each_char`とかを使うらしい  
[str.each in Ruby isn't working](https://stackoverflow.com/questions/2104319/str-each-in-ruby-isnt-working)



## 所感
rubyのHash 慣れない