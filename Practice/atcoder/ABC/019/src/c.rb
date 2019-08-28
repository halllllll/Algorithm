# nが小さいのでなんとなくやってもいけそう
# なんとなくダメそうなやつを省いていく
# にぶたんで存在するか判断して、あったら引く

# と思ったらなんか問題を読み違えていたっぽい
# べつに与えられる配列の[i]と[j]が1:2だったらなんとかする、という意味ではないらしい
# 任意の整数xって書いてあるわ マジか

# 解説みちゃったのでもうそのままやるだけ

# ただの配列にしたためinclude?が時間かかったのか1TLE

n = gets.chomp.to_i
h = {}
gets.chomp.split.map{|a|
  a = a.to_i
  while a.even? do
    a/=2
  end

  if h.has_key?(a).!
    h[a] = true
  end
}
puts h.size