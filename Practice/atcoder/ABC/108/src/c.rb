# 奇数はかんたん 偶数ならkで割ってk/2あまるやつと割り切れるやつのそれぞれ組み合わせしたやつを加算
n, k = gets.chomp.split.map(&:to_i)
ans = 0
if k.odd?
  ans = (n/k).floor ** 3
else
  s = 0
  t = 0
  (1..n).each do |x|
    if x % k  == k / 2
      t += 1
    elsif  x % k == 0
      s += 1
    end
  end
  ans = t ** 3 + s ** 3

end
puts ans
