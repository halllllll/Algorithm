# 全探索する
arr = gets.chomp.split.map(&:to_i)
results = []
arr.size.times do |i|
  for j in (i+1...arr.size) do
    for k in (j+1...arr.size) do
      results << arr[i] + arr[j] + arr[k]
    end
  end
end
results = results.uniq.sort
puts results[-3]