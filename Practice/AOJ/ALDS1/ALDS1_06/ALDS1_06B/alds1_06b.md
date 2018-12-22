## 問題名
Partition
## キーワード
ソート

## 概要
配列の基準を決めて基準から左側に基準より小さい数、右側に大きい数がくるようなソートをする

## 方針と読解
> partition ( A, p, r )は、配列 A[ p..r ] を A[ p..q － 1] の各要素が A[q] 以下で、A[ q +1.. r ] の各要素が A[ q ] より大きい A[ p..q － 1] と A[q + 1..r ] に分割し、インデックス q を戻り値として返します。

らしいのでそれっぽいのを実装する。問題では配列の最後の要素が基準の要素になる

- 配列Aと基準となる要素rが与えられる
- i = -1, 0<=j<len(A)
- A[i]<=A[r]のとき
    - i+=1
    - A[i]とA[j]を交換
- A[r]<A[i]
    - とくになにもしない
### ruby
```ruby
def partition(a)
  length = a.size
  r = length-1
  i = -1
  (0...length).each do |j|
    if a[j] <= a[r]
      i+=1
      # puts "#{a[j]}と#{a[i]}交換"
      a[j], a[i] = a[i], a[j]
    else
      # puts "#{a[r]}<#{a[j]} とくになにもしない"
      next
    end
  end
  return a
end
```

## 参考
該当するページにある擬似コード

## 所感
はい。応用が思いつかん