@n, @a = gets.chomp.split.map(&:to_i)
@arr = gets.chomp.split.map(&:to_i).sort
@count = 0

if @a<@arr[0]
  puts 0
  exit
end

# ダメだったので方針を変えて最後まで探索することにする.
# 配列をもたせるとメモ化できないので、それまでの合計値ももたせる
# 更にそれだけじゃダメなので、今までに取った数ももたせる
@memo = Array.new(50+1).map{|x| Array.new(50+1).map{|x| Array.new(50*50+1, nil)}}
def func(i, j, s)
  if !(@memo[i][j][s].nil?)
    return @memo[i][j][s]
  end
  if i==@n
    # 平均をとる 整数で@aとなることに注意
    if (s.to_f/(j).to_f) == @a.to_f
      return 1
    else
      return 0
    end
  else
    ans = 0 # ?
    # 追加する場合としない場合
    ans += func(i+1, j+1, s+@arr[i]) + func(i+1, j, s)
    #  "i: #{i} j: #{j} s: #{s} に#{ans}をセット"
    @memo[i][j][s] = ans
    return ans
  end
end

puts func(0, 0, 0)

<<~EOS
def func(i, a)
  # iがnのサイズを越えた場合は終了
  # @arrはソート済なので平均は小さくなることはない。越えたら終了
  a_clone = a.clone
  if i==@n-1
    if a_clone.empty?
      return 0
    elsif (a_clone.sum/a_clone.size.to_f) == @a.to_f
      puts "最後に回収 やったぜ"
      return 1
    else
      return 0
    end
  end
  if (a_clone.sum/a_clone.size.to_f) == @a.to_f
    puts "発見 やったぜ"
    return 1
  elsif (a_clone.sum/a_clone.size.to_f) > @a.to_f
    return 0
  else
    ans = 0
    ans += func(i+1, a_clone) + func(i+1, a_clone << @arr[i+1])
    return ans
  end
end

puts func(0, [])+func(0, [@arr[0]])
EOS