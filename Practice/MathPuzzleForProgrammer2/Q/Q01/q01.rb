# じゃんけんルール関係なく3playerで大きいやつが一人勝ちする感じ
count = 0
0.upto(100).each do |goo|
  (0).upto(100-goo).each do |choki|
    par = 100 - goo - choki
    maximum = [goo, choki, par].max
    if [goo, choki, par].count(maximum) == 1
      count += 1
    end
  end
end
puts count