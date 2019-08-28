s = gets.to_i
fn, i = s, 1
if s == 4 || s== 2 || s== 1
  puts 4
  exit
end
arr = [fn]
loop do
  if arr[i-1] % 2 == 0
    arr << arr[i-1]/2
  else
    arr << 3*(arr[i-1])+1
  end
  if arr[i] == 4 || arr[i] == 2 || arr[i] == 1
    puts i+4
    break
  end
  i+=1
end