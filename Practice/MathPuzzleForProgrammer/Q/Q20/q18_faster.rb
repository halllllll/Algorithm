# combination dynamic programming
@fassard = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
sum_n = @fassard.inject(:+)
arr = Array.new(sum_n+1, 0)
arr[0] = 1  # 和が0になるのは1通りだけ
@fassard.each do |fi|
  sum_n.downto(0) do |ai|
    if arr[ai] > 0
      arr[ai+fi]+=arr[ai]
    end
  end
end
sum_max = arr.max
max_index = arr.find_index(sum_max)
puts "多い和 #{max_index} とその数#{sum_max}"