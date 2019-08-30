# 異なる数 -> 大きいほうが左右両端につく 1通り*それぞれの階乗をかけたもの(順列)
# 同じ数 -> 左右が異なるので2通り*それぞれのre
# ぜんぶ整数の掛け算なので都度割っても変わらない

n, m = gets.chomp.split.map(&:to_i)
d = 10**9+7
ans = 1
if n==m
  n.downto(1) do |i|
    # mのぶんもついでにやる
    ans*=i
    ans%=d
    ans*=i
    ans%=d
  end
  puts 2*ans%d
elsif (n-m).abs==1
  # なるべく一緒に処理する
  1.upto([n, m].max) do |i|
    if i<=n
      ans*=i
      ans%=d
    end
    if i<=m
      ans*=i
      ans%=d
    end
  end
  puts ans
else
  puts 0  
end