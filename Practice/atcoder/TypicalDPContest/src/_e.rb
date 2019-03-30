# digit dp
# dぶんもたせてmemo[桁数][越えるかどうか][総和をdで割ったあまり]とするらしい
# 都度割ってあまりだけ乗せていくという戦法
# わざわざrubyのバージョンを合わせてやってもローカルだと動くのに提出したらREになるんだが？？？？？？？？？？？？？？？？？？？？？

@d, @n = gets.chomp.to_i, gets.chomp
@memo = Array.new(@n.size+1).map{Array.new(2).map{Array.new(@d+1, nil)}}


def rec(i, threshold, s)
  if i == @n.size
    return s.zero? ? 1 : 0
  end
  if @memo[i][threshold][s].nil?.!
    return @memo[i][threshold][s]
  end
  ret = 0
  limit = (threshold==1) ? @n[i].to_i : 9
  (0..limit).to_a.each do |j|
    nex_threshold = (j==limit && threshold == 1) ? 1 : 0
    ret += rec(i+1, nex_threshold, (s+j) % @d)
    ret %= 10**9 + 7
    @memo[i][threshold][s] = ret
  end
  return ret
end

puts rec(0, 1, 0) - 1 # 0のぶんを引く