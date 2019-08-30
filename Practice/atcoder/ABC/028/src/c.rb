arr = gets.chomp.split.map(&:to_i).reverse
puts [arr[0]+arr[1]+arr[-1], arr[0]+arr[2]+arr[3]].max