n = gets.to_i
arr = gets.chomp.split.map(&:to_i)
count = 0
(0...n).each do |i|
  mi = i
  (i...n).each do |j|
    # i以降のうちで最小のやつを取る
    if arr[mi] > arr[j]
      mi = j
    end
  end
  # 交換する
  if i != mi
    count += 1
    arr[i], arr[mi] = arr[mi], arr[i]
  end
end
puts arr.map(&:to_s).join(' ')
puts count