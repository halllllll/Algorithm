# 再帰の深さの上限に引っかかるのでなんとかするやつ
if !ENV['RUBY_THREAD_VM_STACK_SIZE']
    #Rubyパスを取得するには、rbconfigかrubygemsを使う。AtCoderでは--disable-gemsされているので、require 'rubygems'は必須である。
    #require 'rbconfig';RUBY=File.join(RbConfig::CONFIG['bindir'],RbConfig::CONFIG['ruby_install_name'])
    require 'rubygems';RUBY=Gem.ruby
    exec({'RUBY_THREAD_VM_STACK_SIZE'=>'100000000'},RUBY,$0) #100MB
end


# 引数にコストを含めない大事（🐜本曰く）
N = gets.to_i
@arr = gets.chomp.split.map(&:to_i)
@table = Array.new(N+1).map{Array.new(3, nil)}
# i番目までで
def rec(i, step)
  return (@arr[i]-@arr[i-step]).abs if i==N-1 # 現在地点が終端なのでstep前との差を返す
  return (@arr[N-1]-@arr[N-2]).abs if i==N  # 現在地点が終端を越えてしまった場合はとうぜん最後の2値の差
  return @table[i][step] if @table[i][step] != nil
  ret = (@arr[i] - @arr[i-step]).abs # 現在地点でのstep前との差
  ret += [rec(i+1, 1), rec(i+2, 2)].min # 次の地点へ移動・ステップ数を意識
  @table[i][step] = ret
  return ret
end

puts [rec(1, 1), rec(2, 2)].min