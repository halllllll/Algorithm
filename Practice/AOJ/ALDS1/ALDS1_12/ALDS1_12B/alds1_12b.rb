# frozen_string_literal: true

# 訪れたかどうかとコスト（と、どこからきたか）をそれぞれ配列でもつ

# どこからスタートするか、ってのを@cost[start] = 0してるんだけどちょっとわかりにくい
# これがのちに「どこからきたか」がわかるってのが直感しにくい
# 配列でもつので、@cost[i]がstartからのコストってのも直感しにくいな...

N = gets.chomp.to_i
# 隣接行列
@graph = Array.new(N).map { Array.new(N, -1) }
@cost = Array.new(N, 10**9) # コスト
@visited = Array.new(N, false) # 訪れたかどうか
@prev = Array.new(N, -1) # いらんけど

N.times do
  input = gets.chomp.split.map(&:to_i)
  i = input[0]
  v = input[1]
  v.times do |vi|
    ti = input[(vi + 1) * 2]
    tc = input[(vi + 1) * 2 + 1]
    @graph[i][ti] = tc
  end
end

# スタート地点は決まっているのでそれを設定
start = 0
@cost[start] = 0
loop do
  mincost = 10**9
  # まず、どこのノードを追加するか決める
  target_node = -1
  N.times do |i|
    # 選定できる条件は「未踏」のうちで最もコストが低いもの
    if @visited[i] == false && @cost[i] < mincost
      mincost = @cost[i]
      target_node = i
    end
  end
  break if target_node == -1

  # 追加するノードが確定したので探索済みとする
  @visited[target_node] = true
  # 追加するノードを選定し、コストを更新
  N.times do |i|
    # 未踏かつエッジがないときは更新できない
    next unless @visited[i] == false && @graph[target_node][i] > 0

    # コスト更新できるかどうか
    next unless @cost[target_node] + @graph[target_node][i] < @cost[i]

    @cost[i] = @cost[target_node] + @graph[target_node][i]
    # ここでどこからきたか更新できる わかりにくいけど
    @prev[i] = target_node
  end
end
N.times do |i|
  puts "#{i} #{@cost[i]}"
end
