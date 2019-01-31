n = gets.to_i
x1, y1, x2, y2, x3, y3 = gets.chomp.split.map(&:to_i)
# (x-x1)^2 + (y-y1)^2 = (x-x2)^2 + (y-y2)^2
# -2*x1*x + x1^2 - 2*y1*y + y1^2 = -2*x2*x + x2^2 - 2*y2*y + y2^2
# 2(x2-x1)*x - 2(y2-y2)*y + x1^2 - x2^2 + y1^2 - y2^2 = 0