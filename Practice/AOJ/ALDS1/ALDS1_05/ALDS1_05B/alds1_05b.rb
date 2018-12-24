n = gets.chomp.to_i
s = gets.chomp.split.map(&:to_i)

$count = 0

# merge sort

def merge(left, right)
  ret = []
  # p "start left: #{left}"
  # p "start right: #{right}"
  loop do
    # p "now ret: #{ret}"
    break if left.size.zero? && right.size.zero?
    # 先頭の小さい方から入れていく
    if left.empty? || (!right.empty? && right.first <= left.first)
      ret << right.shift
    elsif right.empty? || (!left.empty? && left.first <= right.first)
      ret << left.shift
    else
      p "fuck"
      exit
    end
    $count += 1
  end 
  # p "end ret: #{ret}"
  ret
end

def merge_sort(arr)
  return arr if arr.size == 1
  mid = arr.size/2
  left = arr[0, mid]
  right = arr[mid, arr.size/2+1]
  left = merge_sort(left)
  right = merge_sort(right)
  return merge(left, right)
end

merged = merge_sort(s).map(&:to_s).join(' ')
puts merged
puts $count