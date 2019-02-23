# 最大値に近づけるためにそれ以外の二つをインクリメントしていく（二番目に大きいやつと最大値との差ぶんだけ増える）
# 二数が同じ数になったとき最小値は↑を加えたものになっている
# それと最大値との差ぶんだけ+2するが、差が奇数だと越えるので
# いったん最大値を更新してから最初に最大値に到達していた二数をインクリメント
a, b, c = gets.chomp.split.map(&:to_i)
maximum = [a, b, c].max
minimum = [a, b, c].min
mid = (a+b+c)-(maximum+minimum)
aa = maximum-mid
if (maximum - (minimum+aa)).even?
  puts aa+(maximum - (minimum+aa))/2
else
  puts aa+(maximum - (minimum+aa))/2+2
end