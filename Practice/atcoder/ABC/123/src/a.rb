# frozen_string_literal: true

antena = []
5.times { antena << gets.chomp.to_i }
k = gets.chomp.to_i

flag = false
5.times do |i|
  5.times do |j|
    next if i == j

    flag = true if (antena[i] - antena[j]).abs > k
  end
end

puts flag ? ':(' : 'Yay!'
