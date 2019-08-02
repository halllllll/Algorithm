# 値とその出現回数でdictなりして値が大きいやつから採用すりゃいい
# 8 8 8 9 10 10 10 10 11 11など
# -> 失敗 5ケースほど
#    4つ以上あるときにもansをkで更新してしまっていたのがミスかな
# -> 失敗 2ケース....
# 意味不明
# あれか 既に4未満2以上の最大が埋まっているときに4以上のものがきたときの分岐

n = gets.chomp.to_i
arr = gets.chomp.split.map(&:to_i)
dict = {}
arr.each do |a|
  if dict.has_key?(a)
    dict[a]+=1
  else
    dict[a]=1
  end
end
dict = dict.sort.reverse
a, b = 0, 0
ans = 0
dict.each do |k, v|
  break if ans != 0
  if v>=4
    if a!=0
      b = k
    else
      a, b = k, k
    end
  elsif a == 0 && v>=2
    a = k
  elsif a != 0 && v>=2
    b = k
  end
  ans = a*b
end

puts ans