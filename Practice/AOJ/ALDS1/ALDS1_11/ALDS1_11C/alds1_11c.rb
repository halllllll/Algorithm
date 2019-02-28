# unionfindぽいけどもっと単純に答えるらしい
# って思ってやったんだけどTLEなるじゃん は？？？？？？？？？？
# なんかリストを作るときに探索して仲間わけしてるからクエリの判定がO(1)で済むっていうやり方をやってるらしい
n, m = gets.chomp.split.map(&:to_i)
arr = Array.new(n).map{[]}
group = Array.new(n, 0) # これで同じグラフに属するか判断するらしい
# ただし判断するときに、0同士は独立した者同士ってことを考慮する
id = 1  # グループ番号
m.times do
  a, b = gets.chomp.split.map(&:to_i)
  arr[a] << b
  arr[b] << a
  # ここで探索して仲間わけするらしい
  # 違ったわ ぜんぶとってから（3WA）
end

# ここで探索して仲間わけ
n.times do |a|
  stack = [a]
  if group[a].zero?
    group[a] = id
  end
  until stack.empty?
    nex = stack.pop
    arr[nex].each do |i|
      if group[i].zero?
        group[i] = id
        stack << i
      end
    end
  end
  id+=1
end

q = gets.chomp.to_i
q.times do
  a, b = gets.chomp.split.map(&:to_i)
  if group[a] == group[b] && group[a] > 0 && group[b] > 0 # 0同士は独立した者同士
    puts "yes"
  else
    puts "no"
  end
end