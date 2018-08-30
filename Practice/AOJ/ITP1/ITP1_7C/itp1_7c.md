## 問題名
Spreadsheet
## キーワード
多重配列?
## 概要
*r*, *c*および*r\*c*の数値行列が与えられる。row, column方向それぞれに要素の合計、最後に全体の合計を付け足して出力する。
## 方針と読解
二重配列でいけるでしょ。

### ruby
```ruby
r, c = gets.chomp.split.map(&:to_i)
sheet = []
last_culumn = Array.new(c, 0)
last_sum = 0
r.times do |y|
    line = gets.chomp.split.map(&:to_i)
    last_sum += line.sum
    line << line.sum
    sheet << line
    last_culumn = last_culumn.zip(line).map{ |a, b| a + b }
end
last_culumn << last_sum
sheet << last_culumn

sheet.each { |s| puts s.join(" ")}
```
としたのだが、同じサイズの配列の同じインデックス同士を足した配列を作るために`zip`を使って同じインデックス同士の配列を作り、それらに対してsumを取っている。
```ruby
last_culumn = last_culumn.zip(line).map{ |a, b| a + b }
```
また、pythonならばワンライナーで多重配列のcolumnを一行ずつ処理して出力するには、こういう内包表記をよく使うが
```python
[print(" ".join(list(map(str, line)))) for line in sheet]
```
これをrubyでやろうとしてこうなった。
```ruby
sheet.each { |s| puts s.join(" ")}
```
## 参考
[Rubyで配列をベクトル的に足し算したい](https://qiita.com/Kta-M/items/b54f12d3eb49520925e7)
## 所感
転置とかも可能だけどループ回すのめんどくさくなったのでできるだけ簡略化した。