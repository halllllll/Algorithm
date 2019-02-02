# 男女合わせて30人の並びで女が続かないものの総数
# 男o女x
# o -> 次にはoかx
# x -> 次はo

@ans = 0
@N = 30
def calc(arr)
  # return 1 if arr.size == @N
  if arr.size==@N
    @ans+=1
  elsif arr.last == "x"
    next_arr = arr.dup
    next_arr << "o"
    calc(next_arr)
  elsif 
    next_arr1 = arr.dup
    next_arr1 << "o"
    calc(next_arr1)
    next_arr2 = arr.dup
    next_arr2 << "x"
    calc(next_arr2)
  end
end

calc(["o"]) + calc(["x"])
puts @ans

# 動的計画法
# 