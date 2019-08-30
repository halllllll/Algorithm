billdings = Array.new(4).map{Array.new(3).map{Array.new(10, 0)}}
def printstate(b)
    b.each.with_index(1) do |bill, bill_idx|
        bill.each do |floor|
            floor.each do |room|
                print " " + room.to_s
            end
            puts
        end
        if bill_idx != b.size then puts "#"*20 end
    end
end

n = gets.to_i
n.times do
    b, f, r, v = gets.chomp.split.map(&:to_i)
    billdings[b-1][f-1][r-1]+=v
end

printstate(billdings)