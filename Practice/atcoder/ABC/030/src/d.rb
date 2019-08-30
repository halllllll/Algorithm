n, a = gets.chomp.split.map(&:to_i)
k = gets.to_i
arr = gets.chomp.split.map(&:to_i)
# 循環に入ったらそこまでの回数を引いたものを循環の長さで割って余りを求め、循環の配列から値を求める
cnt = 0
circular = []
while k > cnt
  cnt += 1
  if circular.include?(a)
    circular = circular[circular.index(a)..-1]
    idx = (k-cnt) % circular.size
    a = arr[circular[idx]-1]
    break
  else
    circular << a
  end
  a = arr[a-1]
end
puts a