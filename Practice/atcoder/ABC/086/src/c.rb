n = gets.to_i
t, x, y = 0, 0, 0
n.times do
    ct, cx, cy = gets.chomp.split.map(&:to_i)
    t, x, y = (ct-t).abs, (cx-x).abs, (cy-y).abs
    if t>=(x+y) && t%2==(x+y)%2
        next
    else
        puts 'No'
        exit
    end
end

puts 'Yes'