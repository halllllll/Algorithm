@fassard = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
def perm(i, current_arr, source_arr, limit)
  length = source_arr.size
  # return  if length < limit
  if current_arr.size == limit
    @res_arr << current_arr
  else
    i.upto(length) do |j|
      next if i==j
      perm(j, current_arr.clone<<source_arr[j-1], source_arr, limit)
    end
  end
end

sum_table = {}
1.upto(@fassard.size) do |i|
  @res_arr = [] # これだとスコープが保たれるんですね初めて使ったわ
  perm(0, [], @fassard, i)
  @res_arr.each do |res|
    if sum_table.has_key?(res.inject(:+))
      sum_table[res.inject(:+)]+=1
    else
      sum_table[res.inject(:+)]=1
    end
  end
end
most_k, most_v = -1, -1
sum_table.each do |k, v|
  if v > most_v
    most_v = v
    most_k = k
  end
end
puts "多い和 #{most_k} とその数#{most_v}"