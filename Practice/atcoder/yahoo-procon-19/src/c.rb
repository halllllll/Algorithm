# いやわかってるんだ、こんなのを置いたところでせいぜいWAがTLEになるだけだってのは。
# でもいいんだ。DPができないんだ。再帰くらいはできるってことくらい、ちっぽけな自尊心の糧にしてもいいだろう？ 
# その程度で報われるような、チャチな自尊心なんだよ。ぼくが付き合っているのは。
# ごめんな、ジャッジサーバー。

if !ENV['RUBY_THREAD_VM_STACK_SIZE']
    #Rubyパスを取得するには、rbconfigかrubygemsを使う。AtCoderでは--disable-gemsされているので、require 'rubygems'は必須である。
    #require 'rbconfig';RUBY=File.join(RbConfig::CONFIG['bindir'],RbConfig::CONFIG['ruby_install_name'])
    require 'rubygems';RUBY=Gem.ruby
    exec({'RUBY_THREAD_VM_STACK_SIZE'=>'100000000'},RUBY,$0) #100MB
end


@k, @a, @b = gets.chomp.split.map(&:to_i)
# @memo = [@k][10**9] 
# @memo = Array.new(@k).map{Array.new(10**9)}
def dfs(i, ai, c)
  if i==@k
    return ai
  end 
  # ビスケットがa枚未満ならできない操作があるので気をつける
  ret = 0
  if @a>ai
    # 1枚増やすかb枚増やす 
    nc = c>0 ? dfs(i+1, ai+@b, c-1) : 0 # 金
    ret = [dfs(i+1, ai+1, c), nc].max
  else
    # 1枚増やすかb枚増やすかa枚を1円にする
    nc = c>0 ? dfs(i+1, ai+@b, c-1) : 0 # 金
    ret = [dfs(i+1, ai+1, c), dfs(i+1, ai-@a, c+1), nc].max
  end
  # @memo[i][ai][c] = ret 
  return ret
end

puts dfs(0, 1, 0)