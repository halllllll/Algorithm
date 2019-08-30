# dp解
# メモの初期化、最初boolにしてたんだけどダメですわ INFにした

N = gets.chomp.to_i
NGS = 3.times.map{gets.chomp.to_i}
p NGS

@memo = Array.new(N+1).map{Array.new(100, nil)}
@c = 0
# i要らない？
@memo = Array.new(N, nil)
# たどりつく回数がおかしいのでログをとってみる
def rec(n, i, lg)
  @c+=1
  if i==100 || n>N || NGS.include?(n)
    puts "ダメでした #{lg}"
    return 10**9
  # elsif @memo[n].nil?.!
  #   return @memo[n] # これを返しているので、「たどりつけるかどうか」しかわからない？ -> メモ化に関する部分を省いたらやはりそのとおりらしい
  elsif n==N
    puts "#{i}回でたどりつける？？？？"
    p lg
    return i
  else
    ret = 10**9
    1.upto(3).each do |j|
      nex_lg = lg.clone << j
      ret = [ret, rec(n+j, i+1, nex_lg)].min
      # @memo[n] = ret
    end
    return ret
  end
end

# 現状のメモ化（1つだけとる）ではやはり最小回数ではなくたどりつけるかどうかしかわからない
# いやまあ答えはboolなのでそれでいいんだけど、
# もしたどりつけるとした場合の最小回数を知りたいじゃないか...
# p rec(0, 0, [])

# p "count: #{@c}"

# ということで最小回数をとりだすやつ感じにしてみたい
INF = 10**9
@memo = Array.new(N+1).map{Array.new(100, INF)}

# うまくいったっぽい？ログとって確認
# ログもうまくいったんだけど、「たどりつかない場合に最小回数が出せず死ぬ」となるので結局ダメなのでは？
# つまり、結局、この問題は、最小回数を答えるようにしたらうまくいかない設計になっていることがわかる
def rec2(n, i, lg)
    if i==100 || n>N || NGS.include?(n)
      return INF
    elsif @memo[n][i] < INF
      return @memo[n][i]
    elsif n==N
      p lg
      return i
    else
      ret = INF
      1.upto(3).each do |j|
        nex_lg = lg.clone << j
        ret = [ret, rec2(n+j, i+1, nex_lg)].min
        @memo[n][i] = ret
      end
      return ret
    end
end

p rec2(0, 0, [])