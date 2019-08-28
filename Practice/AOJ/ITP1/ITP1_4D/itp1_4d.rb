# frozen_string_literal: true

_ = gets
lis = gets.chomp.split.map(&:to_i)
puts "#{lis.min} #{lis.max} #{lis.sum}"
