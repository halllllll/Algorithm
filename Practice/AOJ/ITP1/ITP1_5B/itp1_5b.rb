# frozen_string_literal: true

loop do
    h, w = gets.chomp.split.map(&:to_i)
    break if (h + w).zero?

    line = '#' * w
    for y in (0...h) do
        # puts "y: #{y}"
        line = y.between?(1, h) ? '#' + '.' * (w - 2) + '#' : line
        puts line
    end
    puts
end
 