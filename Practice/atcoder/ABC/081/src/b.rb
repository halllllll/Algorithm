c, _, arr = 0, gets.chomp, gets.chomp.split.map(&:to_i)
while arr.all?(&:even?)
    c+=1
    arr = arr.map{|n|n/=2}
end 

puts c