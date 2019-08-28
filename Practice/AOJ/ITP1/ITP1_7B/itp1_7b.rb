loop do
    ans = 0
    n, x = gets.chomp.split.map(&:to_i)
    break if (n+x).zero?
    (1..n).each do |a|
        (a+1..[n, x-a].min).each do |b|
            (b+1..[n, x-b].min).each do |c|
                ans += a+b+c==x ? 1 : 0
            end
        end
    end
    puts ans
end