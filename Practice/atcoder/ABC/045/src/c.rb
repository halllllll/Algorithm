# 愚直にやる以外の方法がまっっっっったく浮かばないのだが？？？
# いくつ入れるか+どこにいれるか

# 実装が頭ハゲるかと思った...1時間くらいかかったのでは...

s = gets.chomp.chars.map(&:to_i)
ans = s.map(&:to_s).join.to_i
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

def s(arr, s)
  ai = 0
  ret = 0
  cur = 0
  s.each.with_index do |sv, sidx|
    if ai < arr.size && sidx==arr[ai]
      ret += cur*10+sv
      cur = 0
      ai+=1
      next
    end
    cur *=10
    cur += sv
  end
  ret += cur
  return ret
end

# 入れる場所は0からs.size-1箇所
1.upto(s.size-1) do |i|
  @res_arr = []
  perm(0, [], (0...s.size-1).to_a, i)
  @res_arr.each do |a|
    ans+=s(a, s)
  end
end
p ans

