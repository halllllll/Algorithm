# ん〜？わからん
# 愚直にやっても間に合う...か...?
n = gets.chomp.to_i
arr = gets.chomp.split.map(&:to_i)
n.times do |i|
  tmp_arr = arr[0, i]+arr[i+1, n-1]
  p tmp_arr
  tmp_v = tmp_arr[0]
  ans = 0
  (0...n-1).to_a.each do |j|
    ans += (tmp_v - tmp_arr[j].abs).abs
  end
  # p ans
  puts ans + (tmp_arr[-1]).abs
end