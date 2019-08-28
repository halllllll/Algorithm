n = gets.chomp.to_i
nodes = gets.chomp.split.map(&:to_i)  # one origine
nodes.each.with_index do |v, idx|
  node = "node #{idx+1}: "
  key = "key = #{v}, "
  parent_key = idx > 0 ? "parent key = #{nodes[((idx+1)/2).to_i-1]}, " : ""
  left_key = idx*2+1 < n ? "left key = #{nodes[idx*2+1]}, " : ""
  right_key = idx*2+2 < n ? "right key = #{nodes[idx*2+2]}, " : ""
  puts node + key + parent_key + left_key + right_key
end
