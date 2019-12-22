# 素数かそうでないか、合成数ならば条件に合うかで二回判定すればおわり
require 'prime'

n = gets.chomp.to_i
if Prime.prime?(n) then
  puts "Prime"
  exit
elsif n != 1 then
  s = n.to_s.chars
  t = s.map(&:to_i).inject(:+) % 3
  if ( (s.last.to_i).odd? &&  s.last != "5") && t != 0 then
    puts "Prime"
    exit
  end
end

puts "Not Prime"