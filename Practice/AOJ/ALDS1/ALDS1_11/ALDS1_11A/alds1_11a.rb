n = gets.chomp.to_i

n.times do
  t = gets.chomp.split.map(&:to_i)
  if t[0].zero?.!
    tt = t[2, t[1]]
    arr = Array.new(n, 0)
    tt.each do |ti|
      arr[ti-1] = 1
    end
    puts arr.map(&:to_s).join(" ")
  end
end