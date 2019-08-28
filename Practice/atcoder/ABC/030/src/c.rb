n, m = gets.chomp.split.map(&:to_i)
x, y = gets.chomp.split.map(&:to_i)
a_lis = gets.chomp.split.map(&:to_i)
b_lis = gets.chomp.split.map(&:to_i)
ans = 0
now = 0
def lower_bound(arr, x)
  # arrのうちx以上となる最小の値
  l, r = -1, arr.size
  loop do
    mid = (r + l)/2
    return mid if r - l < 1
    if x <= arr[mid]  # ここで大なりイコールしているので、x以上、が保たれる
      r = mid
    else
      l = mid + 1
    end
  end
end

loop do
  # aからbに向かうことにする
  lb = lower_bound(a_lis, now)
  if lb == -1 # n - 1の場合 泥臭い
    lb = 0
  end
  break if lb >= n
  now = x + a_lis[lb]
  # bからaに向かうことにする
  lb = lower_bound(b_lis, now)
  if lb == -1
    lb = 0
  end
  break if lb >= m
  now = y + b_lis[lb]
  ans += 1
end

puts ans
