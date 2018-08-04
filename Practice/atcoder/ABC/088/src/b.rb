n = gets.to_i
cards = gets.chomp.split.map(&:to_i).sort.reverse
a, b = 0, 0
cards.each.with_index{|v, idx|
    idx.even? ? a+=v : b+=v
}
p a-b