# 座標圧縮的な、インデックスと値を入れ替えるみたいなノリって感じ？
# 座圧、辞書構造を使うのをすっかり忘れてた

n = gets.chomp.to_i
arr = gets.chomp.split.map(&:to_i)
arr_hash = {}
arr.each.with_index do |v, idx|
  arr_hash[v] = idx+1
end
arr_hash = arr_hash.sort_by{|k, _| k}.reverse.to_h
arr_hash.each do |_, v|
  puts v
end
