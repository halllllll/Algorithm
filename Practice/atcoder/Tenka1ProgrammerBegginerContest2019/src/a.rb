# frozen_string_literal: true

# 無能だった 問題文くらい読もう

a, b, c = gets.chomp.split.map(&:to_i)
if a < c && c < b || a > c && c > b
  puts 'Yes'
else
  puts 'No'
end
