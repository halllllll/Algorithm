r, c = gets.chomp.split.map(&:to_i)
sheet = []
last_culumn = Array.new(c, 0)
last_sum = 0
r.times do |y|
    line = gets.chomp.split.map(&:to_i)
    last_sum += line.sum
    line << line.sum
    sheet << line
    last_culumn = last_culumn.zip(line).map{ |a, b| a + b }
end
last_culumn << last_sum
sheet << last_culumn

sheet.each { |s| puts s.join(" ")}