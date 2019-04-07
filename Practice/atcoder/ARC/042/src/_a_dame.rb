# Nが小さいのでシミュレーションで十分
# と思いきや問題文を読み飛ばしてたわ 30点までが100だった
# 満点は5000なので間に合わない
# 配列組み直しでやる
# なんかどうでもいいところでミスってて2WA
# 出力の最初の要素をちゃんとした

n, m = gets.chomp.split.map(&:to_i)
arr = (1..n).to_a
m.times do
  a = gets.chomp.to_i
  next if a==1
  arr = [arr[a-1]] + arr[0, a-1] + arr[a, n]
end
arr.each do |ai|
  puts ai
end