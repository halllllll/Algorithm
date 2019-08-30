## 問題名
Binary search trees - Binary Search Tree I

## キーワード
二分探索木

## 概要
n個のクエリが与えられるからそれに従って二分探索木に挿入/プリントを行う

## 方針と読解
マジでわからんかったので素直に実装を見た。わからん

## 参考
もうわけわからんくてふつうに擬似コード見たんだけどわけわからんくて答えみまくったわ

## 所感
最初配列でやるんかと思ってうごうごしていたのだが、根を基準にして他のノードをparent, left, rightで参照すれば構造体（とかクラス）で済むってワケ。わからんわこんなん。あとこれは八つ当たりですがrubyで書いたら`until`と`unless`を間違えてて丸一日くらい溶かしたよね。二度と使わんぞ。ただしふつうの出力でも構造体の参照がわかりやすくてそこだけはいい

再帰ウザいのでループでやりたい派閥なんだけど、やっぱりというかテストケースが巨大だったらTLEかMLEになる。
```python
# ダメなやつ

def preorder(self):
    # 先行巡回順で出力
    res = []
    cur_node = self.root
    right_successor = []
    left_successor = []
    # 現在の木がなにもない場合
    if cur_node is None:
        return res
    # そうでない場合
    while cur_node is not None:
        res.append(cur_node.key)
        # 次に調べるやつを追加する
        if cur_node.left is not None:
            left_successor.append(cur_node.left)
        if cur_node.right is not None:
            right_successor.append(cur_node.right)
        # 次に調べるやつを左、右の順でやっていく
        cur_node = left_successor.pop() if len(left_successor) > 0 else right_successor.pop() if len(right_successor) else None
    return res

def inorder(self):
    # 中間巡回順で出力
    # 単純にソートでいいのでは
    return sorted(self.preorder())
```