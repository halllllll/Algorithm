def gcd(a, b)
  if a > b
    gcd(b, a)
  end
  # 最大公約数
  d=0
  loop do
    d = b % a
    break if d == 0
    a, b = d, a
  end
  return a
end

def lcm(a, b)
  return (a*b)/(gcd(a, b))
end

loop do
  target = gets
  break if target.nil?
  a, b = target.split.map(&:to_i)
  g = gcd(a, b)
  l = lcm(a, b)
  puts "#{g} #{l}"
end