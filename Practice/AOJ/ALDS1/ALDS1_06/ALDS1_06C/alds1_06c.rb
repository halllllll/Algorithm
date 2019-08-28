def partition(a, l, r)
  pivot = a[r-1][1]
  j = l-1
  (l...r).each do |i|
    if a[i][1] <= pivot
      j+=1
      a[j], a[i] = a[i], a[j]
    end
  end
  return j
end

def quick_sort(a, l, r)
  if 1 < r-l
    q = partition(a, l, r)
    quick_sort(a, l, q)
    quick_sort(a, q+1, r)
  end
end


def merge(a, l, m, r)
  l_arr = a[l, m-l] << ['死', 10000000000000000000]
  l_i = 0
  r_arr = a[m, r-m] << ['死', 10000000000000000000]
  r_i = 0
  
  (l...r).each do |idx|
    # 小さい方から入れていく
    if l_arr[l_i][1] <= r_arr[r_i][1]
      a[idx] = l_arr[l_i]
      l_i+=1
    else
      a[idx] = r_arr[r_i]
      r_i+=1
    end
  end
end

def merge_sort(a, left, right)
  if 1 < right-left
    mid = (right+left)/2
    merge_sort(a, left, mid)
    merge_sort(a, mid, right)
    merge(a, left, mid, right)
  end
end

n = gets.to_i
a = []
n.times do
  a << gets.chomp.split.map{|x| x.match?(/\d/) ? x.to_i : x}
end
b = a.clone
quick_sort(a, 0, n)
merge_sort(b, 0, n)

puts a == b ? "Stable" : "Not stable"
a.each do |av|
  puts "#{av[0]} #{av[1]}"
end