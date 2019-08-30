# 適当に計算するだけ

px1, py1, px2, py2, t, v = gets.chomp.split.map(&:to_f)
n = gets.chomp.to_i
def dist(x1,y1,x2,y2)
  return Math.sqrt((x1-x2)**2 + (y1-y2)**2)
end
n.times do
  x, y = gets.chomp.split.map(&:to_f)
  # 距離を算出
  d = dist(px1, py1, x, y) + dist(px2, py2, x, y)
  if (d/v) <= t
    puts "YES"
    exit
  end
end
puts "NO"