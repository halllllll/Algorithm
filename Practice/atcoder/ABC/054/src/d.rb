N, A, B = gets.chomp.split.map(&:to_i)
@a_arr = []
@b_arr = []
@c_arr = []
N.times do
a, b, c = gets.chomp.split.map(&:to_i)
@a_arr << a
@b_arr << b
@c_arr << c
end

@memo = Array.new(N).map{Array.new(10*40+1).map{Array.new(10*40+1, 0)}}

def rec(i, a, b, c)
  # puts "i: #{i} a: #{a} b: #{b} c: #{c}"
  if i==N
    if a>0&&b>0&&a*B==A*b
      # puts "最後までいって成功 #{c}"
      return c
    else
      return 10000000000000000
    end
  end
  if @memo[i][a][b]>0
    return @memo[i][a][b]
  end
  # return c if a>0 && b>0 && (a/b).to_f == (A/B).to_f
  if a>0 && b>0 && a*B==A*b
    # puts "いい感じの配合に至ったので返す c= #{c}"
    return c
  end
  ret = [rec(i+1, a+@a_arr[i], b+@b_arr[i], c+@c_arr[i]), rec(i+1, a, b, c)].min
  @memo[i][a][b] = ret
  return ret
end

ans = rec(0, 0, 0, 0)
puts ans==10000000000000000 ? -1 : ans
