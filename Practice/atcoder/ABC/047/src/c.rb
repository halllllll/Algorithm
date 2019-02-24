# 2分岐しかしない幅優先
# (右端と左端は別の文字でありWorBのいずれか -> 右端/左端とは別の文字を差し込む)
# とかいって舐めた実装したらTLEなった
<<~EOS
s = gets.chomp
queue = [[s, 0]]
loop do
  q = queue.shift
  if q[0].chars.uniq.size == 1
    puts q[1]
    exit
  else
    left, right = "", ""
    if q[0][0] == "B"
      # 左端にWをぶちこんだシミュレーション
      left = "W" + q[0].chars.map.with_index{|c, idx| idx < q[0].chars.index("W") ? "W" : c}.join("")
    elsif q[0][0] == "W"
      # 左端にBをぶちこんだシミュレーション
      left = "B" + q[0].chars.map.with_index{|c, idx| idx < q[0].chars.index("B") ? "B" : c}.join("")
    end
    if q[0][-1] == "B"
      # 右端にWをぶちこんだシミュレーション
      right = q[0].chars.reverse.map.with_index{|c, idx| idx < q[0].chars.reverse.index("W") ? "W" : c}.join("").reverse + "W"
    elsif q[0][-1] == "W"
      # 右端にBをぶちこんだシミュレーション
      right = q[0].chars.reverse.map.with_index{|c, idx| idx < q[0].chars.reverse.index("B") ? "B" : c}.join("").reverse + "B"
    end
    queue << [right, q[1]+1] << [left, q[1]+1]
  end
end
EOS

# っつって解説みたらなんのこたぁない ただの境界数えだった.....
s = gets.chomp.chars
ans = 0
(1...(s.size)).to_a.each do |i|
  ans += s[i-1]!=s[i] ? 1 : 0
end
puts ans