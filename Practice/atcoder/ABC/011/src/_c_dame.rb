# ダメみたいですね（11WA)
# なんとかしましょうね


















# 最小回数を答えるdpを作ると当然のように無理だった（そもそもたどりつけないときに探しまくるので死ぬ)
# というかそもそも最小回数は関係ない
# なので、どの経路をたどってもたどりつきさえすればよいっていうdp

N = gets.chomp.to_i
NGS = 3.times.map{gets.chomp.to_i}
INF = 10**9
# なぜかnilじゃなくてINFにしたらうまくいかない
@memo = Array.new(N+1, nil)

def rec(n, i)
  if n==79
    puts "はいyes決定"
  end
  if NGS.include?(n) || i==100 || n>N
    return INF
  elsif @memo[n] != nil
    return @memo[n]
  elsif n==N
    return i
  else
    1.upto(3).each do |j|
      ret = rec(n+j, i+1)
      if @memo[n].nil?
        @memo[n] = [ret, INF].min
      else
        @memo[n] = [ret, @memo[n]].min
      end
    end
  end
  return @memo[n]
end

puts rec(0, 0) == INF ? "NO" : "YES"


