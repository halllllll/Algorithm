n = gets.chomp.to_i
a = gets.chomp.split.map(&:to_i)
 
def partition(a)
  length = a.size
  r = length-1
  i = -1
  (0...length).each do |j|
    if a[j] <= a[r]
      i+=1
      # puts "#{a[j]}と#{a[i]}交換"
      if j==r
        a[j] = "[#{a[j]}]"
      end
      a[j], a[i] = a[i], a[j]
    else
      # puts "#{a[r]}<#{a[j]} とくになにもしない"
      next
    end
  end
  return a
end
 
puts partition(a).map(&:to_s).join(' ')