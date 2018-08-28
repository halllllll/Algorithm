loop do 
    h, w = gets.chomp.split.map(&:to_i)
    if (h + w).zero?
        break
    end
    (0...h).each do |i|
        if i.between?(1, h - 2)
            puts '#' + '.' * (w - 2) + '#'
        else
            puts '#' * w
        end
    end
    puts
end