## 問題名
Recursion / Divide and Conquer - The Number of Inversions
## キーワード
再帰、分割統治

## 概要
配列sの反転数を数える。半点数とはi<jかつsi>sjとなる(i,j)の個数である。
## 方針と読解
愚直回答だと1≤n≤200,000なので不可能。O(n^2)。

さっぱりわからんので調べたらALDS1_05Bでやったマージソートが使えるらしい。

つまり、あるタイミングで以下のようになっていたとすると

```
left: [1 5 6 7 11 12]  right: [2 3 4 8 9 10]
```
マージソートのmargeの部分でやったように先頭から小さいやつを取っていくんだけど、1回目が終わった時点でこのようになる
```
left: [5 6 7 11 12]  right: [2 3 4 8 9 10]
ret: [1]
```
次はrightの2なんだけど、**rightから取るってことはleft側のどの要素よりも小さいってことなので、leftのサイズ分だけ反転数のカウントが増える。** 終わった後はこんな感じ
```
left: [5 6 7 11 12]  right: [3 4 8 9 10]
ret: [1 2]
count: 5(+5)
```
で、次もrightのほうが小さいので
```
left: [5 6 7 11 12]  right: [4 8 9 10]
ret: [1 2 3]
count: 10(+5)
```
その次も
```
left: [5 6 7 11 12]  right: [8 9 10]
ret: [1 2 3 4]
count: 15(+5)
```
次からは左なのですっ飛ばすと
```
left: [11 12]  right: [8 9 10]
ret: [1 2 3 4 5 6 7]
count: 15(+0)
```
で右
```
left: [11 12]  right: [9 10]
ret: [1 2 3 4 5 6 7 8]
count: 17(+2)
```
更に
```
left: [11 12]  right: [10]
ret: [1 2 3 4 5 6 7 8 9]
count: 19(+2)
```
もういっちょ
```
left: [11 12]  right: []
ret: [1 2 3 4 5 6 7 8 9 10]
count: 21(+2)
```
というわけ。

### ruby
```ruby
def marge_and_count(left, right)
  ret = []
  tmp_left = left.clone
  tmp_right = right.clone
  loop do
    break if left.empty? && right.empty?
    # 小さい順から取っていく
    if left.empty? || (!right.empty? && right.first < left.first)
      @count += left.size # これ
      ret << right.shift
    elsif right.empty? || (!left.empty? && left.first <= right.first)
      ret << left.shift
    else
      "fuck"
    end
  end
  ret 
end
```
## 参考
- [問題解決のためのプログラミング一巡り](http://www.graco.c.u-tokyo.ac.jp/icpc-challenge/wp-content/uploads/2014/12/2014.pdf)
    - C++での簡易な実装例が載っているが、そこにあるコメントの **「左半分の方が大きい，左半分で未処理の要素だけ飛び越える」** がヒントになった（ぼくはC++書けない）
- [【AOJ ALDS1_5】D: Recursion / Divide and Conquer - The Number of Inversions](https://muttan1203.hatenablog.com/entry/ALDS_1_5_D)
    - そのまんまです。
    - > 反転数は, 対象データが格納されている配列を二分しLとRを作った時, 配列Rの各要素R[j]について, R[j]よりもあとに移動するようなLの要素は, (Lの要素数)-(Lの現在のインデックス)で求められる.
    - 最初にこれ読んでさっぱりわからなかったが↑のやつと比べると意味がわかった。


## 所感
解読できたら嬉しいよね。はい。