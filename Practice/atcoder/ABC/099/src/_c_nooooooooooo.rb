# Nが小さいので一回につき削れるやつを列挙して貪欲できそう
# できませんでした 110だと81*1+9*3+1*2より36*3+1*2のほうが早い
# なので貪欲しつつDFSしつつ最小値を越えたら刈り上げ
# できませんでした
# 素直にdpを組む

n = gets.chomp.to_i
=begin
@koho = [1]
q = 9
loop do
  break if q>n
  @koho << q
  q*=9
end
r = 6
loop do
  break if r>n
  @koho << r
  r*=6
end
@koho.sort!.reverse!
p @koho
@ans = 10**10

def dfs(cur, count)
  return count if cur==0
  return @ans if @ans<count
  p @ans
  @koho.each do |ki|
    next if cur<ki
    @ans = [@ans, dfs(cur%ki, count+cur/ki)].min
  end
  return @ans
end

print(dfs(n, 0))
=end

l9 = 1
dp = []
