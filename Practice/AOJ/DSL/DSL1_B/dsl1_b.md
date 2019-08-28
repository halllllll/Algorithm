## 問題名
Set - Weighted Union Find Trees

## キーワード
重み付きUnion-find tree, disjoint tree

## 概要
q個のクエリが与えられるからそれに従って重み付きUnion-find木を実装する

## 方針と読解
Union-findの各ノードに重みをつける。基本的にUnion-findだが実装的には高速化云々の前に経路圧縮したほうが楽（ランク付けは高さの比較の実装がなんかヤだ、というわがままもある）。

親への重さを表すデータをもたせておき、経路圧縮版の`root(x)`（xの根を再帰的にさかのぼり、帰ってくる過程で親を直接根につなぎかえる関数）でついでに重さも更新するようにする。

注意点として、`unite(x, y, w)`を*xからyへの重さがwになるように併合する*メソッドと考えたときに、**yからxへは-w**となることである。どちら側に向かっての累積和かを間違えないようにする。

## 参考
- https://qiita.com/drken/items/cce6fc5c579051e64fab
    - c++
    - AOJ, ABCの例題がある
- http://at274.hatenablog.com/entry/2018/02/03/140504
    - python3
    - わかりやすい
- http://or3.hatenablog.com/entry/2019/01/11/214019
    - 上記ふたつがわからなかったのでわかるように噛み砕いた
    - python3
- https://www.topcoder.com/community/competitive-programming/tutorials/disjoint-set-data-structures/
    - 重み付きunion-findに関しては載ってないが、union-findの説明。英語がよえめればたぶんわかりやすい（読んでない）
    - SRMの例題がある（解いてない）

## 所感
世に転がっている解説やサンプルがわかりにくすぎてキレたのでわかりやすく記事にしたのだがこの程度に数日かけたのでほんと向いてないんだと思う