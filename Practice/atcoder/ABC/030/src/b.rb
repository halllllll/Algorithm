n, m = gets.chomp.split.map(&:to_f)
n = (n%12)*30+(m*0.5)
m = m*6
puts [(m-n).abs, 360-(m-n).abs].min