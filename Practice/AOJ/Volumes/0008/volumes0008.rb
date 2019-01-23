loop do
  target = gets
  break if target.nil?
  target = target.to_i
  count = 0 
  # a+b+c+d = n
  (0..9).each do |a|
    (0..9).each do |b|
      (0..9).each do |c|
        d = target - (a+b+c)
        if 0<=d && d<=9
          count+=1
        end
      end
    end
  end
  puts count
end