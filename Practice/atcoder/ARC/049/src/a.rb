# なんかふつうに足してく感じ
# 最後にくる場合に気をつける
s = gets.chomp.chars
abcd = gets.chomp.split.map(&:to_i)
ans = ""
aid = 0
s.each.with_index do |sv, idx|
  if abcd[aid] == idx
    ans+="\""
    aid+=1
  end
  ans+=sv
end
if aid==3
  ans+="\""
end
puts ans