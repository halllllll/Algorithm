n = gets.to_i
hash = {}
original_order = []
n.times do
  t = gets.to_i
  original_order << t
  hash[t] = nil
end
hash = hash.sort_by{|k, _| k}.to_h
index = 0 

hash.keys.each do |k|
  hash[k] = index
  index+=1
end

original_order.each do |t|
  puts hash[t]
end