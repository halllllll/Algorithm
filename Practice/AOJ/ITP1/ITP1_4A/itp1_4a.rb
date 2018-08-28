a, b = gets.chomp.split.map(&:to_i)
# 正直最後の小数点以下表示するやつはわからんかった
puts "#{a.div(b)} #{a % b} #{format('%.10f', a.to_f/b)}"