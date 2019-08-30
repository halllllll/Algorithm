# frozen_string_literal: true

r = gets.chomp.to_f
puts "#{format('%.10f', r * r * Math::PI)} #{format('%.10f', r * 2 * Math::PI)}"
