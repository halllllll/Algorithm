# union-find、かと思いきやクエリはなく順序そのままで、Nも小さいのでIDの配列と価値の配列でいけそう
# 「必ず自分より社員番号が小さい上司がただ一人存在する」なので根が高橋くんである木が唯一存在する

n = gets.chomp.to_i
@arr = Array.new(n).map{Array.new()}
@val = Array.new(n, 0)

1.upto(n-1) do |i|
  t = gets.chomp.to_i - 1
  @arr[t] << i
end

def dfs(i)
  target = @arr[i]
  if target.empty?
    @val[i] = 1
    return 1
  else
    minimum = 100000000000000000
    maximum = -1
    ret = 0 # ?????
    target.each do |j|
      # puts "i=#{i}, j=#{j}"
      ret = dfs(j)
      # puts "ret = #{ret}"
      maximum = [maximum, ret].max
      minimum = [minimum, ret].min
    end
    @val[i] = maximum + minimum + 1
    return @val[i]
  end
end

dfs(0)

puts @val[0]