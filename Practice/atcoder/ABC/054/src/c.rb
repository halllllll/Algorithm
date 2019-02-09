# dfs使えばいいんじゃないかな
n, m = gets.chomp.split.map(&:to_i)
graph = Array.new(n).map{[]}
m.times do
  a, b = gets.chomp.split.map(&:to_i)
  graph[a-1] << b-1
  graph[b-1] << a-1
end
# p graph
Track = Struct.new(:nowpath, :visited)

paths = [Track.new(graph[0], [0])]
ans = 0
while paths.size > 0 do
  cur = paths.pop
  ans += cur.visited.size == n ? 1 : 0
  # puts "next available: #{cur.nowpath}"
  cur.nowpath.each do |next_id|
    unless cur.visited.include?(next_id)
      # p cur.visited
      next_track = Track.new(graph[next_id], cur.visited.clone << next_id)
      paths << next_track
    end
  end
end

puts ans