n, m = gets.chomp.split.map(&:to_i)
A = Array.new(n).map{Array.new(gets.chomp.split.map(&:to_i))}
B = Array.new()
m.times do
    B << gets.to_i
end

A.each do |a| 
    c = 0
    a.each_with_index do |aa, idx|
        c += aa*B[idx]
    end
    puts c
end