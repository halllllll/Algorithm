A, B, C = gets.to_i, gets.to_i, gets.to_i
x = gets.to_i
ans = 0
(0..A).each do |a|
    (0..B).each do |b|
        (0..C).each do |c|
            ans+=1 if a*500+b*100+c*50==x
        end
    end
end

puts ans