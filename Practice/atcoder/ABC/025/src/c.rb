# 全然わからんのでググった記事を読みながら書いた
# ゲーム木？要は盤面の状態をもたせただけらしい

@point_v = Array.new(2)
2.times do |i|
  @point_v[i] = gets.chomp.split.map(&:to_i)
end
@point_h = Array.new(3)
3.times do |i|
  @point_h[i] = gets.chomp.split.map(&:to_i)
end

# ゲーム系は最終手番からの探索・貪欲・一発必勝法のどれからしい この場合は最終手番しかなさそう
# 最終手番からの探索とか書いたけどこれ違うわ
# 頭から探索していくんだけどどちらかひとりだけを考えて、自分の手番では最大化、相手の手番では最小化されるような処理をしていく
# これだと一人分の得点しか取れないが、ゲームの仕様上盤面のすべての得点はどちらかに取られる感じになるので
# 他方の得点は合計値から一方を引いたものになる
# 奇数回目でtのターン、盤面は3x3
# 最終手のひとつ手前はaのターン、このとき残っているのは2箇所
# 同様にその一つ手前のtでは3箇所
# とやっていくと最初にtが置く場所9箇所から考えて9!通りある だいたい40万個くらい

# なんかしらんけどダメっぽい 明日の俺覚えてないと思うからセーブするわ





def dfs(i, board_state)
  if i == 9
    # 探索終了して得点を返す
    t_score = 0
    # 高さ方面のスコア
    (0..1).to_a.each do |h|
      (0..2).to_a.each do |w|
        t_score += @point_h[h][w] == board_state[h][w] ? @point_h[h][w] : 0
      end
    end
    # 広さ方面のスコア
    (0..2).to_a.each do |h|
      (0..1).to_a.each do |w|
        t_score += @point_v[h][w] == board_state[h][w] ? @point_v[h][w] : 0
      end
    end
    return t_score
  else
    # 高橋くんの場合だけを考える。
    # つまり（1 originで）奇数ターンは最大化、
    # （1 originで）偶数ターンは最小化
    ret = 0
    if i.odd?
      # 青木ターン、最小化
      minimum = 10**10
      next_board_state = board_state.clone
      (0..2).to_a.each do |h|
        (0..2).to_a.each do |w|
          if next_board_state[h][w] == "-"
            next_board_state[h][w] = "a"
            minimum = [minimum, dfs(i+1, next_board_state)].min
          end
        end
      end
      return minimum
    else
      # 高橋ターン、最大化
      maximum = -1
      next_board_state = board_state.clone
      (0..2).to_a.each do |h|
        (0..2).to_a.each do |w|
          if next_board_state[h][w] == "-"
            next_board_state[h][w] = "t"
            maximum = [maximum, dfs(i+1, next_board_state)].min
          end
        end
      end
      return maximum
    end
  end
end

# 盤面の初期状態
board = Array.new(3).map{Array.new(3, "-")}
maximum = dfs(0, board)