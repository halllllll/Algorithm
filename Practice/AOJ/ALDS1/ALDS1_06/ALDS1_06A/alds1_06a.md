## 問題名
Counting Sort
## キーワード
ソート

## 概要
計数ソートを実装する

## 方針と読解
計数ソート
> 入力数列 A の各要素 Aj について、Aj 以下の要素の数をカウンタ配列 C に記録し、その値を基に出力配列 B における Aj の位置を求めます。
- 最大kであるn個の要素からなる配列Aが与えられる
- k個の要素からなる配列Cを用意して0で初期化
- 配列Aの各要素をAiとするとC[Ai]をインクリメント
    - これでAiの登場回数をカウント
- 空の配列Bを用意
- Cの各要素CiとそのインデックスiとしてCiが0になるまでBにiを追加していく

### ruby
```ruby
def counting_sort(a)
  k = a.max
  c = Array.new(k+1, 0)
  a.each do |ai|
    c[ai] += 1
  end
  b = []
  c.each.with_index do |ci, idx|
    tmp = ci
    loop do
      break if tmp.zero?
      b << idx
      tmp -= 1
    end
  end
  return b
end
```

## 参考
該当するページにある擬似コード

## 所感
擬似コードはなんかしらんけど末尾からループを回してたり、他のコードみたらCを累積和にしてたり意図がわからんのだがふつうにこれでいいじゃんって感じで実装しました