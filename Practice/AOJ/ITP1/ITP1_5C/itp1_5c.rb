loop do
    h, w = gets.chomp.split.map(&:to_i)
    if (h + w).zero?
        break
    end
    (0...h).each do |y|
        line = ""
        (0...w).each do |x|
            line = (y + x).even? ? line + "#" : line + "."
        end
        puts line
    end
    puts
end