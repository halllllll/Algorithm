n = gets.chomp.to_i
arr = gets.chomp.split.map(&:to_i).sort
table = {}
arr.each do |ai|
  if table.has_key?(ai)
    table[ai] += 1
  else
    table[ai] = 1
  end
end
koho = []
# 最頻値の+-1の数とそのtable[+-1]の数を調べる。
# ↑間違い 2 2 2 4 4 5 5 6 6 7 7とか
# なので、出てきたやつを試していく
max_count = 1
koho.each do |mi|
  # puts "#{mi}の周囲"
  count = 0
  [-1, 0, 1].each do |i|
    if table.has_key?(mi+i)
      count+=table[mi+i]
    end
  end
  # puts "#{mi}の周囲の合計 #{count}"
  max_count = [max_count, count].max
end

puts max_count