# なんかしらんけど2つのテストケースで死ぬ なんだよababaって

# 奇数番目と偶数番目でどっちに合わせるかって問題
# ってだけなんだけどなんか複雑なんだけど
# 出てきた回数の多いやつでほかのやつを上書きする
# 値が同じなら回数の多い方、値が異なるならそれぞれその値で上書き
# 値が同じで回数も同じなら異なるやつが出てくるまで探索
# 全部同じだったら「両者とも1種類のみ」か「両者とも同じ数を同じぶんだけもっている」
# - 1種類 一方を総入れ替え n/2
# - まったく同じ 一方を二番目に多いやつで上書き

# ... というふうに手続き的に考えたらめんどくさいのだがわかんなくなってきて解説みたら楽すぎて時間無駄にした感が半端ない

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
# 鬱になる

# そもそも二番目が存在しない（N=2とか一種類だけとか）の場合があるのでそれをまず弾く
if evens.size == 1 && odds.size == 1
  if evens[0][0] == odds[0][0]
    # 値が同じ場合一方を全部上書き
    puts n/2
  else
    # 異なっているので上書きする必要はない
    puts 0
  end
elsif evens.size == 1
  # 他方のやつの「keyが異なるもののうち最大のもの」で上書き
  if odds[0][0] != evens[0][0]
    puts odds[0][1]
  else
    puts odds[1][1]
  end
elsif odds.size == 1
  if evens[0][0] != odds[0][0]
    puts evens[0][1]
  else
    puts evens[1][1]
  end
else
  # 1番目,2番目しか使わないのでシミュレーションするまでもなく、
  # それぞれどちらかを入れてみて小さい方を採用
  o1, o2 = odds[0], odds[1]
  e1, e2 = evens[0], evens[1]
  if o1[0] != e1[0]
    # 両方共最大のやつを使える
    puts n-(o1[1]+e1[1])
  else
    # 一方は1番目、他方は2番目にして最小になるようなやつ
    puts [n-(o1[1]+e2[1]), n-(o2[1]+e1[1])].min
  end
end