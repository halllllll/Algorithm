# 市の6桁はぜんぶ取得してソートしてインデックス入れ替え（座圧的な）
n, m = gets.chomp.split.map(&:to_i)
prefs_citis = {}
citis = []  # 出てきた順番を保存
m.times do
  pi, ci = gets.chomp.split.map(&:to_i)
  citis << [pi, ci]
  if prefs_citis.has_key?(pi)
    prefs_citis[pi] << ci
  else
    prefs_citis[pi] = [ci]
  end
end
prefs_citis.each do |k, v|
  table = {}  # rubyのhashは順番も保つらしい
  v.sort.uniq.each.with_index do |vi, idx|
    table[vi] = idx+1 # 座圧ぽいやつここ
  end
  prefs_citis[k]=table
end
citis.each do |pi, ci|
  kami6 = pi.to_s.rjust(6, "0")
  simo6 = prefs_citis[pi][ci].to_s.rjust(6, "0")
  puts kami6+simo6
end