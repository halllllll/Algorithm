n, m = gets.chomp.split.map(&:to_i)
friends = Array.new(n).map{Array.new()}
m.times do
  a, b = gets.chomp.split.map(&:to_i)
  friends[a-1] << b-1
  friends[b-1] << a-1  
end

<<~EOS
friends.each do |f|
  p f
end
EOS

n.times do |i|
  count = 0
  vec = []
  friends[i].each do |f|  # iの友達
    friends[f].each do |ff| # iの友達fの友達
      if i!=ff && !friends[i].include?(ff)
        vec << ff
        count+=1
      end
    end
  end
  # puts "#{i}の友達の友達: #{vec.map(&:to_s).join(" ")}"
  puts vec.empty? ? 0 : vec.uniq.size
end