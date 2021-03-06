## 問題名
Binary search trees - Binary Search Tree Ⅲ

## キーワード
二分探索木の削除

## 概要
n個のクエリが与えられるからそれに従って二分探索木に挿入/プリント/探索/削除を行う

## 方針と読解
前回（ALDS1_8 B）のやつをそのまま流用してちょろっと加えてやればなんとかなる、と思ったらダメだった。螺旋本の説明やググって出てくる解説はまったく意味をなさないほど何言ってんのかわからんので時間の無駄だった。

一番役に立ったのはなんとwikipediaだった。

## 参考
- http://nihaoshijie.hatenadiary.jp/entry/2018/08/01/020309
> 結構簡単に実装できます。考え方は「次に大きな値を探す」です。次の２つの操作を繰り返します。
> - 右下に木があれば、右下の木の最小値を見つける。
> - 右下に木がなければ、右上の親を探す。

> 二分探索木について言えば、複雑になるのを回避するには実は parent を持たせないほうが良かったりします。


とあったのでparentを持たせないようにしたらアホほどコードが長くなった。もたせたほうがよかった。

- [二分探索木](https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E6%9C%A8)
> 削除ノードが子を二つ持つ場合
> - 削除ノードの左の子から最大の値を探索する。
> - で探索してきたノード（以下、探索ノード）を削除対象のノードと置き換えて、削除対象のノードを削除する。このとき探索ノードの左の子を探索ノードの元位置に置き換える（二分探索木の性質上、探索ノードには右の子は無い）。

とあったのでそのようにした。最初左の木の最大値でやっていたら題意がアレらしく想定解は**右の木の最小値**でないといけない。どっちでもあってんだろが...と思いながら実装する
## 所感
無駄な読解に時間を浪費しまくって得られたものはゼロだった。クソ。親はもたせたほうがいい。