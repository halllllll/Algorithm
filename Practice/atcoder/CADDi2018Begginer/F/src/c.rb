require 'prime'

n, pp = gets.chomp.split.map(&:to_i)
if pp == 1
  puts 1
else
  pd = Prime.prime_division(pp).select{|t| t[1]>=n}
  ans = 1
  pd.each do |pdd|
    ans *= pdd[0]**(pdd[1]/n)
  end
  puts ans
end