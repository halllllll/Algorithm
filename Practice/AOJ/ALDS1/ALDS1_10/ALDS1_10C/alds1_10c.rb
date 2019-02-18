n = gets.to_i

def func(x, y)
  x_l, y_l = x.length, y.length
  dp = Array.new(y_l + 1).map{Array.new(x_l + 1, 0)}
  1.upto(y_l) do |i|
    1.upto(x_l) do |j|
      if y[i-1] == x[j-1]
        dp[i][j] = dp[i-1][j-1]+1
      else
        dp[i][j] = [dp[i-1][j], dp[i][j-1]].max
      end
    end
  end
  return dp[-1][-1]
end

n.times do
  # メソッド側で文字の配列にしていちいち長さを出してたら間に合わなかった
  x = gets.chomp.chars
  y = gets.chomp.chars
  puts func(x, y)
end