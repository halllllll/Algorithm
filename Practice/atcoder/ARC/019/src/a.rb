s = gets.chomp.chars
s = s.map do |si|
  if si == "O"
    "0"
  elsif si == "D"
    "0"
  elsif si == "I"
    "1"
  elsif si == "Z"
    "2"
  elsif si == "S"
    "5"
  elsif si == "B"
    "8"
  else
    si
  end
end
puts s.join("")