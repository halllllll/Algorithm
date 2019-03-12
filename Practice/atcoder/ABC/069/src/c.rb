# 奇数が絡んできた場合だけできない可能性がある
# 奇数の数をk、4の倍数であって2の倍数でない数をfとすると k f k f や f k fはok 
# 2の倍数であって4の倍数でないやつはどっか適当に影響しないとこ（両端とか）においとけばいいので考えないで済む
# ↑間違い 1WA
# 2の倍数であって4の倍数でないやつをbとすると
# k f k f k (S(f)-1>=S(k))は大丈夫だが
# b b k f k f k b b b とかはダメ
# 
# S(f)>=S(k)

n = gets.chomp.to_i
odd_n, two_n, four_n = 0, 0, 0
gets.chomp.split.map(&:to_i).each do |ai|
  if ai.odd?
    odd_n+=1
  elsif ai%4==0
    four_n+=1
  else
    two_n+=1
  end
end
if four_n>=odd_n-1 && two_n == 0
  puts "Yes"
elsif four_n>=odd_n
  puts "Yes"
else
  puts "No"
end