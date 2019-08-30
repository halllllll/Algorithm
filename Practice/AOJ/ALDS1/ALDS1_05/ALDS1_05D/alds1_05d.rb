n = gets.chomp.to_i
a = gets.chomp.split.map(&:to_i)

@count = 0

def marge_and_count(left, right)
  ret = []
  tmp_left = left.clone
  tmp_right = right.clone
  loop do
    break if left.empty? && right.empty?
    # 小さい順から取っていく
    if left.empty? || (!right.empty? && right.first < left.first)
      @count += left.size # これ
      ret << right.shift
    elsif right.empty? || (!left.empty? && left.first <= right.first)
      ret << left.shift
    else
      "fuck"
    end
  end
  ret 
end

def rec(arr)
  # リストごと渡してくれるわ
  return arr if arr.size == 1
  mid = arr.size/2
  left = arr[0, mid]
  right = arr[mid, arr.size/2+1]
  left = rec(left)
  right= rec(right)
  marge_and_count(left, right)
end

rec(a)
p @count