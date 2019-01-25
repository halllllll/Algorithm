r, c, k = gets.chomp.split.map(&:to_i)
# 全体のマップ
table = Array.new(r).map{Array.new(c, false)}
# r行目・c列目にいくつブツがあるか
row_arr, column_arr = Array.new(r, 0), Array.new(c, 0)
n = gets.to_i
n.times do
  # データを各配列に保存
  y, x = gets.chomp.split.map(&:to_i)
  table[y-1][x-1] = true
  row_arr[y-1]+=1
  column_arr[x-1]+=1
end
p row_arr
p column_arr

# ki個ある行・列数を数える（ki個ある行・列はそれぞれいくつあるか）
row_dict = (0..k).to_a.map{|x|[x, 0]}.to_h
column_dict = (0..k).to_a.map{|x|[x, 0]}.to_h
row_arr.each{|ri| row_dict[ri]+=1 }
column_arr.each{|ci|column_dict[ci]+=1}
ans = 0

# table[y][x]の状態は2種類に分けられる。すなわち、table[y][x]にブツがあるかないかによって、である。ブツがあるとき、行[y]と列[x]においてブツを重複して数えていることになる。自明だが、table[y][x]にブツが無い場合は重複は存在するはずがない。逆に、重複が無い場合はtable[y][x]にブツは存在しない、ということがいえる。
# ただし、「重複している場合を含んでもkと等しくなる」場合がある、という事象とは別で考える。たとえば、以下の問題が相当する。
# Q:「すべてのブツの総量が7、行[3]におけるブツの総数が4、列[5]におけるブツの総数が1、列[10]におけるブツの総量がであるとき、行*列=10*10の取り得るtableを示せ」
# A: 書いたら分かるはず* 雑..................................


(0..k).each do |ki|

end

# 行yと列xの交差点である、table[y][x]を考える。table[y][x]の状態は、ブツがあるかないかの二つになる。
# table[y][x]にブツがないとき、table[y][x]における題意を満たすブツkは、(y行目のブツの数)+(x列目のブツの数)=kとなるtable[y][x]の組[y][x]の総数である。行yと列xを別々に
# table[y][x]にブツがあるときは、
#   - table[y][x] = kのとき、これは行[y]に含まれるブツの総数と列[x]に含まれるブツの総数の和であり、かつブツのうちのひとつは（条件「table[y][x]にブツがあるとき」から自明のとおり）table[y][x]にある。行[y]と列[x]はそれぞれ別にそのブツを数えているので、計上が重複している。すなわち、【*あとで書く】において
# 