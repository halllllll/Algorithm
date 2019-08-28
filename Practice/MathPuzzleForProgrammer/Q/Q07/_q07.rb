# 注:なぜか最後の日付の出力ができなかったのでこのコードはクソです

# Dateが使えるっぽい
require 'date'
# 1964/10/10から2018/7/24まで
# ２進数の逆転の10進数なのでそもそも偶数の日付は該当しないのは自明
d = Date.new(1964, 10, 10)+1
g = Date.new(2018, 7, 24)
c = 0
while d < g do
  b = d.to_s.split('-').join.to_i.to_s(2)
  if b==b.reverse
    puts "#{d.to_s}"
    c+=1
  end
  d+=2
end
puts c