# frozen_string_literal: true

n = gets.chomp.to_i
s = gets.chomp.chars
k = gets.chomp.to_i
t = s[k - 1]

ans = ''
s.each do |c|
  ans += if c == t
           c
         else
           '*'
         end
end

puts ans
