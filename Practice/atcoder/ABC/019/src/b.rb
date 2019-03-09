# 原因不明の1WA
# 原因不明の2WA...?
# まったく同じロジックのやつをpythonでやったら通ったのでバグ？
# （rubyのバージョン違い由来ならREなるだろうし）

s = gets.chars
ans = ""
tmp = s[0]
count = 1
(s.size-1).times do |i|
  if s[i+1] == tmp
    count+=1
  else
    ans+=tmp+count.to_s
    tmp = s[i+1]
    count = 1
  end
end

# 帳尻合わせ
puts ans+s[-1]+count.to_s+"\n"