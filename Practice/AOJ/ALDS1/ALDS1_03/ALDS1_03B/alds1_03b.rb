# 余った分は考えないらしい
n, q = gets.chomp.split.map(&:to_i)

queue = []

n.times do
  queue.push(gets.chomp.split.map{|x| x.match?(/^\d+$/) ? x.to_i : x})
end
# 入力された順に処理する
# FIFOは頭からいれてケツから出すという意識があるので
queue.reverse!
count = 0 # 経過時間
loop do
  break if queue.size.zero?
  # rubyではケツから取り出すのはpop
  t = queue.pop
  count += [t[1], q].min
  t[1] = [0, t[1]-q].max
  if t[1].zero?
    puts "#{t[0]} #{count}"
  else
    # rubyでは先頭にぶちこむのはunshift
    queue.unshift(t)
  end
end

