# digit DPを使う おしまい
# 範囲がAからなので、
# 「A~Bまでの数」 -> 「(0~Bまでの数)-(0~A-1までの数)」にする

a, b = gets.chomp.split

memo_until_a = Array.new(a.size+1).map{Array.new(2).map{Array.new(2, nil)}}
memo_until_b = Array.new(b.size+1).map{Array.new(2).map{Array.new(2, nil)}}

def rec(n, memo, i, threshold, flag)
  if i==n.size
    return flag
  end
  if memo[i][threshold][flag].nil?.!
    return memo[i][threshold][flag]
  end
  ret = 0
  limit = threshold == 1 ? n[i].to_i : 9
  (0..limit).to_a.each do |j|
    nex_threshold = (j==limit && threshold == 1) ? 1 : 0
    nex_flag = (flag==1 || [4, 9].include?(j)) ? 1 : 0
    ret += rec(n, memo, i+1, nex_threshold, nex_flag)
    memo[i][threshold][flag] = ret
  end
  return ret
end

puts rec(b, memo_until_b, 0, 1, 0) - rec((a.to_i-1).to_s, memo_until_a, 0, 1, 0)
