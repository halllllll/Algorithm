# めんどくさいので1つのケースだけにするためにuppercaseする。
# 最後に.がつくのはアリにする
n = gets.chomp.to_i
arr = gets.chomp.split.map(&:upcase)
count = 0
arr.each do |a|
  if a=="TAKAHASHIKUN" || a=="TAKAHASHIKUN."
    count += 1
  end
end
puts count