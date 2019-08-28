# なぜかダメだった方法（前post参照）の原因がわからんので視点を変える
# nから配列は同定されるのでそれと与えられる配列を比較する

n = gets.chomp.to_i

# nから題意の配列を導出するマシーン
def f(n)
  if n.odd?
    return [0] + (2..n-1).each_slice(2).map(&:first).map{|ai| [ai, ai]}.flatten
  else
    return (1..n-1).each_slice(2).map(&:first).map{|ai| [ai, ai]}.flatten
  end
end

arr_origin = f(n)

# マシーンと比較するためソート
arr_target = gets.chomp.split.map(&:to_i).sort
if arr_origin == arr_target
  puts n.even? ? 2**(n/2) % (10**9+7) : 2**((n-1)/2) % (10**9+7)
else
  puts 0
end