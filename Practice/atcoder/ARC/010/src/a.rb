# まあそんな感じの算数をやる感じです
# ただ単に書いてある感じの算数

n, m, a, b = gets.chomp.split.map(&:to_i)
m.times do |i|
  if n<=a
    n+=b
  end
  target = gets.chomp.to_i
  if n<target
    puts i+1
    exit
  else
    n-=target
  end
end
puts "complete"