arr = Array.new(Math.sqrt(1000000).to_i+1, true)
arr[0], arr[1] = false, false
primes = []
(2..arr.size).each do |i|
  if arr[i] == true
    primes << i
    (i*2).step(arr.size, i) do |j|
      arr[j] = false
    end
  end
end

loop do
  target = gets
  break if target.nil?
  target = target.to_i
  count = 0
  primes.each do |pr|
    if target<pr
      break
    end
    count+=1
  end
  puts count
end