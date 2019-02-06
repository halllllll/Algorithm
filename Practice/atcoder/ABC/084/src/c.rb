n = gets.to_i

c, s, f = [], [], []
(n-1).times do
  ci, si, fi = gets.chomp.split.map(&:to_i)
  c << ci
  s << si
  f << fi
end
c << 0
s << 1
f << 1
# なんとなくシミュレーションする
# 終点だったら終了
# (次の待ち時間)+次への乗車時間
# - 次の発車時間 == 到着時間 -> すぐ乗れる
# - 到着時間 < 次の始発 -> 始発に乗る
# - それ以外（待ち時間） -> 到着時間 + （到着時間-(到着時間/発車間隔+1)*発車間隔）
n.times do |i|
  now = 0
  (i...n-1).each do |j|
    if now < s[j]
      now = s[j]
    elsif (now % f[j]).zero?
      # なにもしない
    else
      # now += now-(now/f[j+1]+1)*f[j+1]
      # now = now + f[j+1]-now%f[j+1] # (now/f[j+1]+1)*f[j+1]
      now = now + f[j]-now%f[j] # (now/f[j+1]
    end
    now += c[j]
  end
  puts now
end