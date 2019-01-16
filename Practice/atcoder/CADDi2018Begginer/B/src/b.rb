N, H, W = gets.chomp.split.map(&:to_i)
ans = 0
N.times do
  h, w = gets.chomp.split.map(&:to_i)
  if h < H || w < W
    next
  else
    ans+=1
  end
end

puts ans