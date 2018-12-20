n = gets.chomp.to_i
a = gets.chomp.split.map(&:to_i)

def counting_sort(a)
  k = a.max
  c = Array.new(k+1, 0)
  a.each do |ai|
    c[ai] += 1
  end
  b = []
  c.each.with_index do |ci, idx|
    tmp = ci
    loop do
      break if tmp.zero?
      b << idx
      tmp -= 1
    end
  end
  return b
end

puts counting_sort(a).map(&:to_s).join(' ')