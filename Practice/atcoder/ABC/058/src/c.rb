# 最初の文字列を基準に各文字と数をマップして、次からは使える文字を使えるだけ使うことにして減らしていく
n = gets.chomp.to_i
table = {}
gets.chomp.chars.each do |c|
  if table.has_key?(c)
    table[c]+=1
  else
    table[c]=1
  end
end
(n-1).times do
  # 基準になってるやつと共通するやつだけ考えればいい
  table_share = {}
  gets.chomp.chars.each do |c|
    if table.has_key?(c)
      if table_share.has_key?(c)
        table_share[c]+=1
      else
        table_share[c]=1
      end
    end
  end
  # 共通するやつの数を少ない方に合わせる
  table.keys.each do |k|
    if table_share.has_key?(k)
      # ここミスって1WA
      table[k] = [table[k], table_share[k]].min
    else
      table[k] = 0
    end
  end
end

# 残ったやつから辞書順で最小のやつを作る
ans = ""
table.keys.sort.each do |k|
  ans += k*table[k]
end
puts ans