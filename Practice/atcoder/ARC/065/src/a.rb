s = gets.chomp
while true
    break if s.size<5
    if ["dream", "erase"].include?(s[-5, 5])
        s = s[0, s.size-5]
        next
    elsif "eraser" == s[-6, 6]
        s = s[0, s.size-6]
        next
    elsif "dreamer" == s[-7, 7]
        s = s[0, s.size-7]
        next
    else
        break
    end
end

puts  s.size==0 ? 'YES' : 'NO'