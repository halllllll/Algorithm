n = 10
@c = 0

def f(a, b)
  return if b[-1] < a[-1]
  if a[-1] == b[-1]
    @c += 1
  else
    (1..4).each do |aa|
      (1..4).each do |bb|
        f(a + [a[-1] + aa], b + [b[-1] - bb])
      end
    end
  end
end


f([0], [n])
p @c
