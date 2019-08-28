n = gets.to_i
arr = gets.chomp.split.map(&:to_i)

max_t = -100000
n.times do |i|
  wakaran = []
  n.times do |j|
    next if i == j
    if j < i
      wakaran << arr[j, i-j+1]
    else
      wakaran << arr[i, j-i+1]
    end
  end
  max_a = -1000000
  target = []
  wakaran.each do |w|
    # atcoderはrubyに対して無理解なのか、なぜか2.3を未だに使っているため、
    # Enumerable::sumが使えず、injectで合計を求めている
    temp_max_a = w.select.with_index{|_ ,idx| idx.odd?}.inject(:+)   # zero order
    if max_a < temp_max_a
      max_a = temp_max_a
      target = w
    end
  end
  # atcoderはrubyに対して無理解なのか、なぜか2.3を未だに使っているため、
  # Enumerable::sumが使えず、injectで合計を求めている
  max_t = [max_t, target.select.with_index{|_, idx| idx.even?}.inject(:+)].max # zero order
end
puts max_t
