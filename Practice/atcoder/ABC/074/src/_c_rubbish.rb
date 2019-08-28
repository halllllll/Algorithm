# 全探索 is どうする
# 最大でもF<=3000, 100<=A, 100<=Bなので30回くらい

# な に か が お か し い
A, B, C, D, E, F = gets.chomp.split.map(&:to_i)
@maximum = -1

ab_set = []
(0..30).to_a.each do |a|
  (0..30).to_a.each do |b|
    next if a*100*A+b*100*B>F || a*100*A+b*100*B==0
    ab_set << [a*A*100.0, b*B*100.0]
  end
end
maximum_e = -1.0
p ab_set
abcd = [-1, -1, -1, -1]
ab_set.each do |a, b|
  (0..30).to_a.each do |c|
    (0..30).to_a.each do |d|
      c, d = c*C.to_f, d*D.to_f
      next if (a+b+c+d)>F
      e = (100*(c+d)/(a+b+c+d))
      next if e > E
      if e > maximum_e
        maximum_e = e
        abcd = [a, b, c, d]
      end
      maximum_e = [maximum_e, e].max
    end
  end
end
puts maximum_e
p abcd
puts
puts "#{(abcd.inject(:+)).to_i} #{(abcd[2]+abcd[3]).to_i}"