# 安いやつから買い占めていく
# 少ないのでwhileしてもいいんだと思う多分

n, m = gets.chomp.split.map(&:to_i)
set = []
n.times do
  set << gets.chomp.split.map(&:to_i)
end
set = set.sort_by{|s| s[0]}
cost = 0
amount = 0
idx = 0
while amount < m do
  if set[idx][1] == 0
    idx+=1
    next
  end
  amount += 1
  cost += set[idx][0]
  set[idx][1]-=1
end
puts cost