# 潰してから復元する方針

h, w = gets.chomp.split.map(&:to_i)
table = []
h.times do
  table << gets.chomp.chars
end

def repaint(map, i, j, mark)
  # map[i][j]とその周囲8マスをmarkに塗り替える
  place = [-1, 0, 1]
  place.each do |y|
    place.each do |x|
      if 0<=i+y && i+y<map.size && 0<=j+x && j+x<map[0].size
        map[i+y][j+x] = mark
      end
    end
  end
end

# tableの「#」を潰す用
pre_table = Array.new(h).map{Array.new(w, "無")}
# pre_tableから処理した結果を復元する用
epi_table = Array.new(h).map{Array.new(w, ".")}

(0...h).each do |i|
  (0...w).each do |j|
    if table[i][j] == "."
      # 処理前は"."の周囲は"."であったはず
      repaint(pre_table, i, j, ".")
    end
  end
end

(0...h).each do |i|
  (0...w).each do |j|
    if pre_table[i][j] == "無"
      # pre_tableにとって"."で潰せなかった場所から"#"が広まるはず
      pre_table[i][j] = "#"
      # epi_tableはpre_tableの処理後の姿
      repaint(epi_table, i, j, "#")
    end
  end
end

if epi_table == table
  puts "possible"
  pre_table.each do |pt|
    puts pt.join("")
  end
else
  puts "impossible"
end