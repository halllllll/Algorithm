## 問題名
Dynamic Programming - Longest Common Subsequence

## キーワード
DP, LCS, 最長部分文字列

## 概要
二つの文字列のLCSを求める

## 方針と読解
参考参考

## 参考
- [http://rudora7.blog81.fc2.com/blog-entry-1095.html](http://rudora7.blog81.fc2.com/blog-entry-1095.html)
- [https://programgenjin.hatenablog.com/entry/2019/03/11/081428](https://programgenjin.hatenablog.com/entry/2019/03/11/081428)

## 所感
**Longest Common Subsequence**と**Longest Common Substring**がどっちもLCSでややこしい。後者のは一致する最長の部分文字列。文字列のままやったらTLEを二回くらったのでクソ。

余談だが数列の場合でその範囲で昇順に並んでいる最長の部分列を**Longest Increasing Subsequence**とかいう。やったことないので知らん（なんかにぶたん使うらしい）

はるか昔に理解してなるほど〜となっていたメモが見つかったが、もう思いっきり忘れててクソ。

DPの処理的にどういった原理で処理していくのかっていう方針みたいなのは無視していいのかもしれない、少なくともナップザックとかの理解が浅いままこれをやっても全然理解できないと思われるし、使う場面が限定されてる（特定の問題に特化してる）タイプであり、汎用性がよくわからん。なので、問題として出されたときに「覚えてないけど貼って終わり」になりそう（これはdisです）。