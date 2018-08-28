# frozen_string_literal: true

a, b, c = gets.chomp.split.map(&:to_i)
ans = 0
a.upto(b) do |x|
  ans = (c % x).zero? ? ans + 1 : ans
end
puts ans
