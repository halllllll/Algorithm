n = gets.chomp.to_i
table = {"JPY"=>0.0, "BTC"=>0.0}
n.times do
  input = gets.chomp.split
  table[input[1]] += input[0].to_f
end

puts table["JPY"]+table["BTC"]*380000.0