# aojをpythonでやろうとしたらダメだったので..
# ↑ >0じゃなくて>=0じゃった

Edge = Struct.new(:s, :t, :cost)  # pythonよりrubyのが優れてるところこれ
n = gets.chomp.to_i
edges = []
n.times do |i|
  line = gets.chomp.split.map(&:to_i)
  n.times do |j|
    if line[j] >= 0
      edges << Edge.new(i, j, line[j])
    end
  end
end
edges = edges.sort_by{|e| e.cost}
@parents = (0...n).to_a
def root(x)
  if x == @parents[x]
    return x
  else
    @parents[x] = root(@parents[x])
    return @parents[x]
  end
end
def unite(a, b)
  a, b = root(a), root(b)
  if a!=b
    @parents[b] = a
  end
end
ans = 0
edges.each do |e|
  u, v = e.s, e.t
  if root(u) != root(v)
    unite(u, v)
    ans+=e.cost
  end
end
puts ans