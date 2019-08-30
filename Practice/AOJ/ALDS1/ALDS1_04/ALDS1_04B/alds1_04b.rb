n = gets.chomp.to_i
s = gets.chomp.split.map(&:to_i)
q = gets.chomp.to_i
t = gets.chomp.split.map(&:to_i)

def func(arr, target)
  left = 0
  right = arr.size
  while left < right do
    mid = (left+right)/2
    if arr[mid] == target
      return true
    end
    if target < arr[mid]
      right = mid
    else
      left = mid + 1
    end
  end
  return false
end
cnt = 0
t.each do |i|
  cnt +=  1 if func(s, i)
end
puts cnt