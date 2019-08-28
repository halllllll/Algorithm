X = gets.chomp.to_i
NGS = 3.times.map{gets.chomp.to_i}
INF = 10**9
@memo = Array.new(X+1).map{Array.new(100, nil)}

def rec(n, i)
  if i==100 || n>X || NGS.include?(n)
    return INF
  elsif @memo[n][i].nil?.! && @memo[n][i] <= s
    return @memo[n][i]
  elsif n==X
    return i
  else
    ret = INF
    1.upto(3).each do |j|
      ret = [ret, rec(n+j, i+1)].min
      @memo[n][i] = ret
    end
    return ret
  end
end

p rec(0, 0) == INF ? "NO" : "YES"