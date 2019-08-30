europastyle = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
americastyle = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]

def count(arr, n)
  t = arr.size - n + 1
  max = 0
  t.times do |i|
    max = [max, arr[0, n].sum].max
    top = arr.shift
    arr << top
  end
  max
end

c = 0
(2..36).each do |i|
  c += 1 if (count(europastyle, i) < count(americastyle, i))
end
p c