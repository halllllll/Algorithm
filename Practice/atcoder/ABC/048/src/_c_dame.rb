# わからんけどdpっぽい
# dpの組み方わからんけどノリで
# dp[左からi番目][左からi番目でjの値]

# ふたつずつみていって、あふれたぶんだけ両方に振り分けていって全探索
# 最初からXより大きいやつはどうせ狩るので最初にとっちゃう 最後に足せばいい

N, X = gets.chomp.split.map(&:to_i)
kubikari = 0

C = gets.chomp.split.map(&:to_i).map do |ci|
  if ci>X
    kubikari += ci-X
    X
  else
    ci
  end
end
@memo = Array.new(N).map{Array.new(10, nil)}
def rec2(i, a, b, s)
  if i==N-1
    return s
  elsif @memo[i][a].nil?.!
    return @memo[i][a]
  else
    if (a+b)<=X
      return rec2(i+1, b, C[i+1], s)
    else
      ret = 10**9
      afure = (a+b) - X
      0.upto(afure) do |n|
        changed_a = a - n
        changed_b = b - (afure-n)
        ret = [rec2(i+1, changed_a, changed_b, s+afure), ret].min
        @memo[i][a]=ret
      end
      return ret
    end
  end
end


puts rec2(0, C[0], C[1], 0)+kubikari