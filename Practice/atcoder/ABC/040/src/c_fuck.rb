@n = gets.to_i
@arr = gets.chomp.split.map(&:to_i)
@arr = @arr.unshift(@arr[0])
# は？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
# メモ化できないんだが？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
# @visited = Array.new(@n+1).map{Array.new(10**6+1, false)}  # i番目までにcostでたどり着く
# @memo = Array.new(@n+1).map{Array.new(10**6+1, 10**11+1)}
@visited = Array.new(@n+1).map{Array.new(2, false)}
@memo = Array.new(@n+1).map{Array.new(2, 10**9)}
<<~EOS
def step(i, cost)
  return cost if i<=0
  return @memo[i][cost] if @visited[i][cost]
  one = step(i-1, cost+(@arr[i]-@arr[i-1]).abs)
  two = step(i-2, cost+(@arr[i]-@arr[i-2]).abs)
  @visited[i][cost] = true
  ret = [one, two].min
  @memo[i][cost] = ret
  return ret
end
EOS
<<~EOS
は？？？？？？？？？？？？？？？？？？？？？？？？
def step(i, oneortwo)
  return (@arr[@n-1]-@arr[i-oneortwo]).abs if i==@n-1
  return (@arr[@n-1]-@arr[@n-2]).abs if i==@n
  return @memo[i][oneortwo-1] if @visited[i][oneortwo-1]
  ret = (@arr[i]-@arr[i-oneortwo]).abs # ?
  one = step(i+1, 1)
  two = step(i+2, 2)
  @visited[i][oneortwo-1] = true
  ret += [one, two].min
  @memo[i][oneortwo-1] = ret
  return ret
end
EOS

def step(n, bef)
  return (@arr[@n-1]-@arr[@n-bef]).abs if n==@n-1
  return (@arr[@n-1]-@arr[@n-2]).abs if n==@n
  return @memo[n][bef-1] if @visited[n][bef-1]
  @visited[n][bef-1] = true
  ret = (@arr[n]-@arr[n-bef])
  ret += [step(n+1, 1), step(n+2, 2)].min
  @memo[n][bef-1] = ret
  return ret
end
puts [step(2, 1), step(3, 2)].min