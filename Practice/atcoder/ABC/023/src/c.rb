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
# ただし、「重複している場合を含んでもkと等しくなる」場合がある、という事象とは別で考える。たとえば、k=1で行[y]に含まれるブツの数が1, 列[x]に含まれるブツの数が1で、table[y][x]にブツがあるとすると、行[y]列[x]ともに唯一のブツをtable[y][x]で共有していることになる。k=2で行[y]のブツが1、列[x]のブツが2でtable[y][x]にブツがある場合は行[y]には列[x]と共有しているもの以外にもうひとつブツがある。
# 「重複している場合にk+1となる」場合は

# 合計値がkになる数を数える。これは合計値がkになる座標と等しい。合計値は上記のtable[y][x]==k

# 全体を数えた（座標を順番に数え上げると間に合わないので配列で計算する）総和から、座標上のブツの位置で
(0..k).each do |ki|

end

# 行yと列xの交差点である、table[y][x]を考える。table[y][x]の状態は、ブツがあるかないかの二つになる。
# table[y][x]にブツがないとき、table[y][x]における題意を満たすブツkは、(y行目のブツの数)+(x列目のブツの数)=kとなるtable[y][x]の組[y][x]の総数である。行yと列xを別々に
# table[y][x]にブツがあるときは、
#   - table[y][x] = kのとき、これは行[y]に含まれるブツの総数と列[x]に含まれるブツの総数の和であり、かつブツのうちのひとつは（条件「table[y][x]にブツがあるとき」から自明のとおり）table[y][x]にある。行[y]と列[x]はそれぞれ別にそのブツを数えているので、計上が重複している。すなわち、【*あとで書く】において
# 