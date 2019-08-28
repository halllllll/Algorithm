c = 1
while x = gets.chomp.to_i do
    if x == 0 then
        break
    end
    puts "Case #{c}: #{x}"
    c+=1
end