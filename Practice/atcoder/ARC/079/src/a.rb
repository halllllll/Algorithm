# frozen_string_literal: true

# 中間となるやつを印つけてく
# 同じクエリがきたらアウトなんで、to/fromをもたせなきゃいけないんだけど
# もうめんどくさいのでuniqするわ

N, M = gets.chomp.split.map(&:to_i)
chukan = N.times.map { false }
flag = false
query = M.times.map { gets.chomp.split.map(&:to_i) }.uniq
query.each do |q|
  to, from = q
  next unless to == 1 || from == N

  target = to == 1 ? from : to
  if chukan[target - 1] == true
    flag = true
    break
  else
    chukan[target - 1] = true
    end
end
puts flag ? 'POSSIBLE' : 'IMPOSSIBLE'
