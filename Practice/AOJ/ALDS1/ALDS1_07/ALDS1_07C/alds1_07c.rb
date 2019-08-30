# 根節点、左部分木、右部分木の順で節点の番号を出力する。これを木の先行順巡回 (preorder tree walk) と呼びます。
# 左部分木、根節点、右部分木の順で節点の番号を出力する。これを木の中間順巡回 (inorder tree walk) と呼びます。
# 左部分木、右部分木、根節点の順で節点の番号を出力する。これを木の後行順巡回 (postorder tree walk) と呼びます。

n = gets.to_i

# rubyにも構造体（というクラス）があるらしいので使ってみる
Node = Struct.new(:id, :left, :right, :parent)
# Array.new(n, Node.new)だと同じ構造体を参照してしまうので
nodes = Array.new(n).map{Node.new}
n.times do
  data = gets.chomp.split.map(&:to_i)
  node = Node.new(*data)
  node.parent = nodes[data[0]].parent
  nodes[data[0]] = node
  nodes[data[1]].parent = node.id if data[1] != -1
  nodes[data[2]].parent = node.id if data[2] != -1
end

def preorder(par, nodes, order)
  # 中間 左 右
  # 中間から子を探索して存在するやつをたどっていく
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
# 根を同定
root = nodes.select{|nd| nd.parent.nil?}[0].id
# preoder
preoder_res = []
preorder(root, nodes, preoder_res)
puts "Preorder"
puts " #{preoder_res.map(&:to_s).join(' ')}"
# inorder
inorder_res = []
inorder(root, nodes, inorder_res)
# 2 1 3 0 6 5 7 4 8
puts "Inorder"
puts " #{inorder_res.map(&:to_s).join(' ')}"
# postorder
postorder_res = []
postorder(root, nodes, postorder_res)
#  2 3 1 6 7 5 8 4 0
puts "Postorder"
puts " #{postorder_res.map(&:to_s).join(' ')}"