# マップでカウントしておく
# 頭文字の組み合わせそれぞれに対して頭文字それぞれの数を掛ける
# なので組み合わせさえ出せれば解ける
# （なんかしらんけど1TLE出した（原因不明）ので一部書き直した）

n = gets.chomp.to_i
@table = {"M"=>0, "A"=>0, "R"=>0, "C"=>0, "H"=>0}

n.times do
  name = gets.chomp
  if @table.has_key?(name[0])
    @table[name[0]]+=1
  end
end

@march = []

def perm(i, current_arr, source_arr, limit, length)
  return  if length < limit
  if current_arr.size == limit
    @march << current_arr
  else
    i.upto(length) do |j|
      next if i==j
      perm(j, current_arr.clone<<source_arr[j-1], source_arr, limit, length)
    end
  end
end

perm(0, [], ["M", "A", "R", "C", "H"], 3, 5)

ans = 0
@march.each do |march|
  a, b, c = march
  ans += @table[a]*@table[b]*@table[c]
end

puts ans