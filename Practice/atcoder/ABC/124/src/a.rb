a, b = gets.chomp.split.map(&:to_i)
ans = 0
2.times do
  if a>b
    ans+=a
    a-=1
  elsif a<b
    ans+=b
    b-=1
  else
    ans+=a
    a-=1
  end
end
puts ans