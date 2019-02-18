# 考察してないけど
n = gets.to_i
arr = gets.chomp.split.map(&:to_i).uniq.sort
if arr.include?(1)
  puts 1
  exit
end

(0...n-1).to_a.each do |i|
  a, b = arr[i], arr[i+1]
  if (b%a).zero?
    arr[1] = arr[0]
  elsif (b%a) == 1
    puts 1
    exit
  else
    arr[1] = a
  end
  arr.shift
end
puts arr[0]
