## 問題名
Tree - Tree Walk
## キーワード
二分木, 木の巡回
## 概要
二分木のノード番号とその子のノード番号が与えられるからPreorder, Inorder, Postorderの順に巡回したときに通るノードを順番にそれぞれ出力
## 方針と読解
はい。構造体に持たせるのは自身のIDと左の子のIDと右の子のIDだけでいいらしいけどノリで自身の親のIDも持たせておいたよ。それぞれのNodeを添字と対応させた配列を用意して巡回していく。よくわからんままに言われたとおりに実装していけば、単に再帰のどのタイミングで自身のIDを出力するかの違いであると分かる。


### ruby
```ruby
Node = Struct.new(:id, :left, :right, :parent)
nodes = Array.new(n).map{Node.new}
-------
# 以下メソッド
def preorder(par, nodes, order)
  order << par
  if nodes[par].left != -1
    preorder(nodes[par].left, nodes, order)
  end
  if nodes[par].right != -1
    preorder(nodes[par].right, nodes, order)
  end
end

def inorder(par, nodes, order)
  if nodes[par].left > -1
    inorder(nodes[par].left, nodes, order)
  end
  order << par
  if nodes[par].right > -1
    inorder(nodes[par].right, nodes, order)
  end
end

def postorder(par, nodes, order)
  if nodes[par].left > -1
    postorder(nodes[par].left, nodes, order)
  end
  if nodes[par].right > -1
    postorder(nodes[par].right, nodes, order)
  end
  order << par
end
```
## 参考
特に螺旋本見ずとも、結果的にほぼ答えと同じような作りになった。

## 所感
はい 無駄に時間喰いました。