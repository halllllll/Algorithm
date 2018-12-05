## 問題名
Allocation
## キーワード
Binary Search

## 概要
省略 ([これ](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D&lang=jp))

## 方針と読解
**最大値の最小値**とか**最小値の最大値**とかきたらだいたいバイナリサーチ。

初期値のleftとright(最小値と最大値)は、それぞれ配列の最大値と制約上の最大値を入れる。その範囲で決め打ちしていって、その値で詰め込めるかどうかをシミュレーションしていく。その部分はpythonで書くとこんな感じ
```python
amount = 0
count = 1
for wi in w:
    if amount+wi > mid:
        count += 1
        amount = wi
    else:
        amount += wi
if count > k:
    # 今のmだと🚙の台数が足りない
    left = mid + 1
else:
    # 今のmで🚗の台数が足りる
    right = mid
```

## 参考
なし

## 所感
最初rubyで書いて3時間ほど溶かした挙げ句にまったくできなかったんだけどキレる前にpythonに切り替えてやったら10分くらいでできた...マジでお前...俺...お前...