n, q = gets.chomp.split.map(&:to_i)
arr = Array.new(n, 0)
q.times do
  l, r = gets.chomp.split.map(&:to_i)
  arr[l-1]+=1
  if r<n
    arr[r]-=1
  end
end
print arr[0].odd? ? 1 : 0
(1...n).each do |i|
  arr[i] += arr[i-1]
  print arr[i].odd? ? 1 : 0
end
puts