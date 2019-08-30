n, y = gets.chomp.split.map(&:to_i)
ans = Array.new(3){-1}
catch :otoshidama do
    0.upto(2000) do |i|
        0.upto(2000) do |j|
            k = n-(i+j)
            break if k<0
            if 10000*i+5000*j+1000*k==y
                ans = [i, j, k]
                throw :otoshidama
            end
        end
    end
end

puts ans.join(' ')