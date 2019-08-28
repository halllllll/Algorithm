# 3で割ります
# -> 割れました -> おわり NHK
# -> 割れません -> 商を越えるまでwかhをageていって近い方を抜く
# 2で割ります
# -> 割れました -> おわり NHK
# -> 割れません -> 商を越えるまでre
# って手続き的に考えて実装したんだけどどうにもうまくいかんし自尊心が死んだので諦めた

# 解説みたらパターンで全探索らしい は？

h, w = gets.chomp.split.map(&:to_i)
def f(h, w)
  minimum = 10**10
  1.upto(h-1) do |hi|
    sa = hi*w
    # 横に分割
    sb = (w/2)*(h-hi)
    sc = h*w-(sa+sb)
    # 適当に分割しただけなのでこれら3つからa,b,cを同定
    # puts "横に分割"
    # p [sa, sb, sc]
    ssc, ssa = [sa, sb, sc].minmax
    minimum = [minimum, ssa-ssc].min
    # 縦に分割
    sb = ((h-hi)/2)*w
    sc = h*w-(sa+sb)
    # 適当に略
    # puts "縦に分割"
    # p [sa, sb, sc]
    ssc, ssa = [sa, sb, sc].minmax
    minimum = [minimum, ssa-ssc].min
  end
  return minimum
end

puts [f(h, w), f(w, h)].min
