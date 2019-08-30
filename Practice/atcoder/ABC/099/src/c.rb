# 最初ふつうにgreedyしててダメだったのでメモ再帰しようとしたんだけど[100000][8?][5?]みたいな感じにしようとしてダメで解説みたけど異次元
# ggったらけんちょんさんのqiitaがあった
# memo 1000000で通ったかどうかだけみればいいっぽい
# あらかじめ取り得る6^pと9^pを用意しておくようにしたがこれはべつにどうとでもなるので単なる趣味
# qiitaのほうで昇順で試してるんだけどこれはcppだから実現できるのかな？(試しにreverseなしでやったらダメだった)

n = gets.chomp.to_i
@memo = Array.new(n+1, -1)
@numset = [1]
roku = 6
while roku<=n
  @numset<<roku
  roku*=6
end
kyu = 9
while kyu<=n
  @numset<<kyu
  kyu*=9
end

# 1から始めるとそりゃあ間に合わんのは当然なので
@numset.sort!.reverse!

def rec(cur)
  return 0  if cur.zero?
  return @memo[cur] if @memo[cur]>0
  ret = 10**10
  @numset.each do |ni|
    if cur>=ni
      ret = [ret, rec(cur-ni)+1].min
    end
  end
  @memo[cur] = ret
  return ret
end

puts rec(n)
