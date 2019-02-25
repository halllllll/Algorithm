# n*2までの平方数を記録していき、都度更新する
# と思ったけどこれ必要あるか....?ふつうに都度計算でもいいような気がするが
# と思ったけど、どのタイミングで増やせばいいかとかどの数使えばいいいかとかは都度やってても当然わからんので予めある程度の数を生成しておくのがいいのか。
def gen_square_num_list(n)
  # ということで都度計算
  ret = []
  1.upto(n).each do |i|
    ret << i*i
  end
  ret
end

# 円順列なのでどれかを固定する並び(順列) (n-1)! これもめんどくさいので都度計算でええやろこんなもん
@n = 4  # こっからスタートすりゃええやろ どうせ2なんてないけど

# メソッド内でぜんぶ作ろうとしたらなんか配列入れ子になっちゃって二次元におとしこめなかったので外にある配列に追加していくハメに...
def gen_comb(n, arr, used)
  if arr.size == n
    # return arr
    @comb_arr << arr
  end
  # ret = []
  (0...n).to_a.each do |ni|
    next if used[ni]
    nex_used = used.clone
    nex_used[ni] = true
    nex_arr = arr.clone
    nex_arr << ni
    # ret  gen_comb(n, nex_arr, nex_used)
    gen_comb(n, nex_arr, nex_used)
  end
  # return ret
end

# ここからスタート

@square_num = gen_square_num_list(30) # なんかテキトーな数だけ べつに根拠はない
@comb_arr = []  # どうせ更新するし

def check(n)
  @comb_ar = []  # ほら更新した
  used_arr = Array.new(@n, false)
  used_arr[0] = true
  gen_comb(@n, [], used_arr)
  # 現段階の@comb_arrの隣り合う要素の差をとってみる
  @comb_arr.each do |ca|
    flag = true
    (0...n).to_a.each do |i|
      diff = ca[i]+ca[(i+1)%n]
      if @square_num.include?(diff)
        next
      end
      flag = false
      break
    end
    if flag
      p ca
      return flag
    end
  end
  return false
end

loop do
  break if check(@n) || @n>6
  @n+=1
end