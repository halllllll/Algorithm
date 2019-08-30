# frozen_string_literal: true

# ダメじゃん

# 例5が非常にいい視点を与えてくれた
# 次元を落として考えると簡単になるので
# まずどちらかの軸だけでフィルターして
# それをもとに他方の軸でカウント

Point = Struct.new(:x, :y, :id, :color)
reds = []
blues = []
N = gets.chomp.to_i
N.times.map do |i|
  x, y = gets.chomp.split.map(&:to_i)
  point = Point.new(x, y, i, 'red')
  reds << point
end
N.times.map do |i|
  x, y = gets.chomp.split.map(&:to_i)
  point = Point.new(x, y, i, 'blue')
  blues << point
end
amount = 0
koho = []
(reds + blues).sort_by(&:x).each do |point|
  if point.color == 'red'
    amount += 1
  else
    if amount > 0
      amount -= 1
      koho << point
    end
  end
end
amount = 0
c = 0
(reds + blues).sort_by(&:y).each do |point|
  if point.color == 'red'
    amount += 1
  else
    if amount > 0
      amount -= 1
      c += 1 if koho.include?(point)
    end
  end
end
puts c
