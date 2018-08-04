n, a, b = gets.chomp.split.map(&:to_i)
c = 0
(1..n).each do |x|
    keta = 0
    temp_x = x
    while x>0
        keta+=x%10
        x/=10
    end
    c+=temp_x if (a..b).include?(keta)
end
p c