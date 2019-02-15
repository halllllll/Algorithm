n = gets.to_i
arr = []
n.times{arr << gets.chomp}
ok = ["M", "A", "R", "C", "H"]
arr = arr.select{|x| ok.include?(x[0])}.uniq
table = {"M"=>0, "A"=>0, "R"=>0, "C"=>0, "H"=>0}
arr.each{|a|table[a[0]]+=1}
table = table.values.select{|t|t>0}
p table
if arr.size<=2
  puts 0
elsif arr.size==3
  puts 1
elsif arr.size==4
  puts 4
elsif arr.size==5
  puts 10
end