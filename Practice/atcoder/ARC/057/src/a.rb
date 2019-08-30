# どうすんだと思ってたんだけどサンプルみると超小さいからそのままやっても大丈夫そう
# k=0の場合のみ1が加えられるだけ

a, k = gets.chomp.split.map(&:to_i)
ans = 0
if k.zero?
  ans = 2*10**12 - a
else
  while a < 2*10**12
    ans+=1
    a+=(a*k)+1
  end
end
puts ans