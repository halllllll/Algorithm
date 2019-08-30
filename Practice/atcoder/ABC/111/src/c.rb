# 2WA
n = gets.to_i
evens = {}
odds = {}
gets.chomp.split.map(&:to_i).each.with_index do |ai, i|
  if i.even?
    if evens.has_key?(ai)
      evens[ai]+=1
    else
      evens[ai]=1
    end
  else
    if odds.has_key?(ai)
      odds[ai]+=1
    else
      odds[ai]=1
    end
  end
end
# 回数で決定するのでソート
evens = evens.sort_by{|_, v| -v}
odds = odds.sort_by{|_, v| -v}
# こっからいろいろめんどくさくなって解説見たやつ
# どうせ順番に多いやつをとっていく戦法でみていっても使うのは1番大きいやつと二番目に大きいやつなのでそれとってきて実際に上書きしてためして小さい方が答えっていう
if evens[0][0]!=odds[0][0]
  # 最大の回数となる値がそれぞれ異なるのでそれぞれその値を使って他の値を上書きできる
  puts n-(evens[0][1]+odds[0][1])
elsif evens.size == 1 || odds.size == 1
  # 一種類しかない場合（N=2 or 完全に一致）
  if evens.size == 1 && odds.size == 1
    # 最大の値が異なっていれば変える必要なし
    # 同じだったら他方をまるごと上書き
    if evens[0][0] != odds[0][0]
      puts 0
    else
      puts n/2
    end
  elsif evens.size == 1
    # 他方の1番目の値が同じなら2番目のやつで上書き
    if evens[0][0] == odds[0][0]
      puts n/2 - odds[1][1]
    else
      puts n/2 - odds[0][1]
    end
  elsif odds.size == 1
    # 他方の1番目の値が同じなら2番目のやつで上書き
    if odds[0][0] == evens[0][0]
      puts n/2 - evens[1][1]
    else
      puts n/2 - evens[0][1]
    end
  end
else
  # 両方共種類が2つ以上ある かつ 最大の値が同じ
  # 1番目に大きいもの、2番目に大きいものをそれぞれとって上書きした場合の最小値
  o1, o2 = odds[0][1], odds[1][1]
  e1, e2 = evens[0][1], evens[1][1]
  puts [n-(o1+e2), n-(o2+e1)].min # まさかのminし忘れ
end
