# 典型メイズ最短
# なので末尾から追加と末尾から探索ですね

# のはずなのだがなぜかサンプルの最後のやつが通らない これはどう考えてもおかしい

h, w = gets.chomp.split.map(&:to_i)
sy, sx = gets.chomp.split.map(&:to_i)
gy, gx = gets.chomp.split.map(&:to_i)
table = Array.new(h)  # for Maze
h.times do |y|
  table[y] = gets.chomp.chars
end
count_table = Array.new(h).map{Array.new(w, -1)} # for count table

table[sy-1][sx-1] = "s"
table[gy-1][gx-1] = "g"
count_table[sy-1][sx-1] = 0

Pos = Struct.new(:y, :x, :c)
first = Pos.new(sy-1, sx-1, 0)
queue = [first]

loop do
  cur_pos = queue.pop()
  steps = [0, 1, 0, -1, 0]
  4.times do |i|
    nex_x = steps[i]+cur_pos.x
    nex_y = steps[i+1]+cur_pos.y
    if table[nex_y][nex_x] == "g"
      puts cur_pos.c+1
      count_table.each do |t|
        p t
      end
      exit
    end
    if table[nex_y][nex_x] == "."
      table[nex_y][nex_x] = "#"
      nex_c = count_table[cur_pos.y][cur_pos.x]+1
      count_table[nex_y][nex_x] = nex_c
      nex_pos = Pos.new(nex_y, nex_x, nex_c)
      queue << nex_pos
    end
  end
end