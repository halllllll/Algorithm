h, w = gets.chomp.split.map(&:to_i)
# 回数が偶数か奇数かで分けられる 奇数->裏返し 偶数->変わらず
# 奇数になるのはどちらも3以上のときorいずれかが1のとき
# 前者では外周以外が奇数になる
if h==1 && w == 1
  puts 1
elsif h==1 || w==1
  puts [h, w].max-2
elsif h==2 || w==2
  puts 0
else
  puts h*w-(2*w+2*(h-2))
end