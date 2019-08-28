# 左側と右側の長さそれぞれk-1（末端から伸ばすぶんで-1）で削っていく感じ
# とおもったけどこれじゃ不十分で, 2 1 3でK=3のとき一発でいけるんでダメ
# 頭からk個、そこからk-1個ずつ伸ばしていく感じ。idxはもはや関係ない
# たぶんO(1)あるんだろうけど思いつかない、せいぜいN<=100000なのでシミュレーションまわしてもいいのでは

n, k = gets.chomp.split.map(&:to_i)
arr = gets.chomp.split.map(&:to_i)

length = 0
count = 0
while length<n do
  if length.zero?
    length = k
  else
    length += k-1
  end
  count+=1
end

puts count