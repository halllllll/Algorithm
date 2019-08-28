# frozen_string_literal: true

# dp with dfs ?

N = gets.chomp.to_i
@arr = []
N.times do
  @arr << gets.chomp.to_i 
end

@dp = {}

def dfs(i, r, g, b)
  return @dp[[r, g, b]] if @dp.key?([r, g, b])

  if i == N
    sanpen = [r, g, b].sort
    if sanpen[0] > 0 && sanpen[2] < sanpen[0] + sanpen[1]
      return 1
    else
      return 0
    end
  else
    ret = 0
    ret += dfs(i + 1, r + @arr[i], g, b)
    ret += dfs(i + 1, r, g + @arr[i], b)
    ret += dfs(i + 1, r, g, b + @arr[i])
    @dp[[r, g, b]] = ret % 998_244_353
    return @dp[[r, g, b]]
  end
end

puts dfs(0, 0, 0, 0)
