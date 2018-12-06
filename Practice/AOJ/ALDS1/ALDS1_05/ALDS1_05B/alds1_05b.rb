n = gets.chomp.to_i
s = gets.chomp.split.map(&:to_i)

$count = 0

# marge sort

def marge(left, right)
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

def marge_sort(arr)
  return arr if arr.size == 1
  mid = arr.size/2
  left = arr[0, mid]
  right = arr[mid, arr.size/2+1]
  left = marge_sort(left)
  right = marge_sort(right)
  return marge(left, right)
end

marged = marge_sort(s).map(&:to_s).join(' ')
puts marged
puts $count