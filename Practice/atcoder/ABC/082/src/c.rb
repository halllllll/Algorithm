# 出てきた順に辞書に追加してインクリメント
# N<=10^5なので余裕
# 数えるのは「足りないのですべて消す」「溢れた分だけ消す」

n = gets.to_i
table = {}
gets.chomp.split.map(&:to_i).each do |i|
  if table[i].nil?
    table[i] = 1
  else
    table[i] += 1
  end
end

c = 0 
table.each do |k, v|
  if !(v.zero?)
    if k<v
      c += v-k
    elsif v<k
      c += v
    end
  end
end

puts c