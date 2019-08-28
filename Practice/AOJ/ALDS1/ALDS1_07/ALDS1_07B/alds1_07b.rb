n = gets.to_i

class Node
  attr_accessor :id, :parent, :left, :right, :sibling, :degree, :depth, :height, :node_type
  def initialize(i)
    @id = i
    @parent = -1
    @left = -1
    @right = -1
    @depth = 0
    @height = 0
    @sibling = -1
    @degree = -1
  end
end

nodes = {}
# 大きさが分かるので初期化しておく
n.times do |i|
  nodes[i] = Node.new(i)
end

# 高さを決める
def height_rec(par, nodes)
  l, r = 0, 0
  if nodes[par].left >= 0
    tmp_left = nodes[par].left
    l = height_rec(tmp_left, nodes) + 1
  end
  if nodes[par].right >= 0
    tmp_right = nodes[par].right
    r = height_rec(tmp_right, nodes) + 1
  end
  nodes[par].height = [r, l].max
end

# 深さを再帰的に更新
def depth_rec(par, nodes)
  left_child = nodes[par].left
  if left_child >= 0
    nodes[left_child].depth = nodes[par].depth + 1
    depth_rec(left_child, nodes)
  end
  right_child = nodes[par].right
  if right_child >= 0
    nodes[right_child].depth = nodes[par].depth + 1
    depth_rec(right_child, nodes)
  end
end

n.times do |i|
  data = gets.chomp.split.map(&:to_i)
  my_id = data[0]
  child_l = data[1]
  child_r = data[2]
  # 子データをセット
  nodes[my_id].left = child_l
  nodes[my_id].right = child_r
  # 子に親と兄弟データをセット
  if child_l >= 0
    nodes[child_l].parent = my_id
    if child_r >= 0
      nodes[child_l].sibling = child_r
    end
  end
  if child_r >= 0
    nodes[child_r].parent = my_id
    if child_l >= 0
      nodes[child_r].sibling = child_l
    end
  end
  # 子の数をセット
  nodes[my_id].degree = [child_l, child_r].select{|c|c!=-1}.size
  # 深さ更新
  depth_rec(my_id, nodes)
end

# 高さ計算とタイプ確定
# root、internal node、leaf 
nodes.each do |k, node|
  height_rec(k, nodes)
  if node.parent == -1
    node.node_type = "root"
  elsif node.degree.zero? 
    node.node_type = "leaf"
  else
    node.node_type = "internal node"
  end
end

# 出力
# node id: parent = p , sibling = s , degree = deg, depth = dep, height = h, type
nodes.each do |k, node|
  puts "node #{node.id}: parent = #{node.parent}, sibling = #{node.sibling}, degree = #{node.degree}, depth = #{node.depth}, height = #{node.height}, #{node.node_type}"
end