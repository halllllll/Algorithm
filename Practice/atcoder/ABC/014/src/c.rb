# どっかでみたな〜〜と思ってたんだけどいもす法の公式の問題例そのままな感じでいけそう
# 「出入りのみで管理する」系（そんなものがあるのかは知らない）
# そもそもいもす法を忘れていたので読み直したけど。

n = gets.chomp.to_i
arr = Array.new(10**6+1+1, 0)
# set
n.times do
  s, e = gets.chomp.split.map(&:to_i)
  arr[s]+=1
  arr[e+1]-=1 # よくよく読んだら以上~以下だったので+1
end
# ちゃんとするフェーズ（用語不明）
arr.size.times do |i|
  next if i==0
  arr[i] += arr[i-1]
end
# で 最大値を取るフェーズ
maximum = -1
arr.each do |ai|
  maximum = [maximum, ai].max
end
puts maximum