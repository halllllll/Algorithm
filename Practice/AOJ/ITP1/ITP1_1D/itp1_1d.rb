S = gets.to_i
h = S / (60 * 60)
m = S % (60 * 60) / 60
s = S % 60
puts [h, m, s].join(':')