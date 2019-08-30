# hashして2つ以上出てくるやつをフィルタリングして逆順ソートして頭からなめていって
# 先に「2つ以上が2つ」「4つ以上が1つ」どちらかが出てきたらそれ

N = gets.chomp.map(&:to_i)
A = gets.chomp.split.map(&:to_i)
h = Hash.new()
A.each do |a|
  if h.has_key?(a)
    h[a] += 1
  else
    h[a] = 1
  end
end