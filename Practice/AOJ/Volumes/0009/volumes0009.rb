include Math

#素数の配列を返すメソッド
def fetch_prime_list(max)
  table = Array.new(max + 1,true)
  prime_list = []

  (2..max).each do |num|
      if table[num] == true
        prime_list << num
      k = num * num
      while k <= max
        table[k] = false
        k += num
      end
    end
  end
  return prime_list
end

def lower_bound(arr, target)
  l, r = 0, arr.size
  while r-l>=1 do
    mid = (r+l)/2
    if arr[mid] <= target # targetを含むので
      l = mid + 1
    else
      r = mid
    end
  end
  return (r+l)/2
end


#配列を返すメソッド
prime_arr = fetch_prime_list(1000000)

loop do
  target = gets
  break if target.nil?
  target = target.to_i
  idx = lower_bound(prime_arr, target)
  puts prime_arr[0, idx].size
end