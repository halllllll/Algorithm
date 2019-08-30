# A(x1, y1), B(x2, y2), C(x3, y3), D(x4, y4)
# Aを原点としたときにBが第n象限にいるかで場合分け
x1, y1, x2, y2 = gets.chomp.split.map(&:to_i)
tx, ty = (x1-x2).abs, (y1-y2).abs
if x1<=x2 && y1<=y2
    # 第1象限
    x3, y3 = x2-ty, y2+tx
    x4, y4 = x1-ty, y1+tx
    puts "#{x3} #{y3} #{x4} #{y4}"
elsif x1>=x2 && y1<=y2
    # 第2象限
    x3, y3 = x2-ty, y2-tx
    x4, y4 = x1-ty, y1-tx
    puts "#{x3} #{y3} #{x4} #{y4}"
elsif x1>=x2 && y1>=y2
    # 第3象限
    x3, y3 = x2+ty, y2-tx
    x4, y4 = x1+ty, y1-tx
    puts "#{x3} #{y3} #{x4} #{y4}"
elsif x1<=x2 && y1>=y2
    # 第4象限
    x3, y3 = x2+ty, y2+tx
    x4, y4 = x1+ty, y1+tx
    puts "#{x3} #{y3} #{x4} #{y4}"
end