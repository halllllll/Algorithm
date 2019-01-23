# ax+by=c, dx+ey=f
# y=(c-ax)/b
# y=(f-dx)/e
# (c-ax)/b = (f-dx)/e
# e(c-ax) = b(f-dx)
# x(bd-ae) = bf-ec
# x = (bf-ec)/(bd-ae)

loop do
  target = gets
  break if target.nil?
  a, b, c, d, e, f = target.split.map(&:to_f)
  x = ((b*f - e*c)/(b*d - a*e)).round(4)
  y = ((c-a*x)/b).round(4)
  x = x.zero? ? x.abs : x
  y = y.zero? ? y.abs : y 
  puts sprintf("%.3f %.3f", x, y)
end