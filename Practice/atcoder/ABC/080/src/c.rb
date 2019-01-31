@n = gets.to_i
@shop_opens = []
@n.times do 
  @shop_opens << gets.chomp.split.map(&:to_i)
end

@shop_points = []
@n.times do
  @shop_points << gets.chomp.split.map(&:to_i)
end

# 各店の開店してる同じ時間帯に開店した回数ぶんだけポイントになる、これを全店でやったポイントの総数の最大値を答える
# -> 開店する時間帯の決め方は月~金それぞれ午前午後で、とりうるすべての組み合わせは2^10程度なのでこれを全探索する
# 開店/閉店は1と0で表されるのを利用してビット演算してANDとる方法もあるがビット演算を調べるのがめんどくさいので愚直に配列でやろうと思う

@ans = -10000000000 # これ桁がたりず2WA...まじかよ

time_period = Array.new(10, 0)

def rec(arr, idx)
  if idx>=10
    # 各店で同じ時間帯に開いてる数から利益を算出して比較アンド更新
    if arr.uniq != [0]
      # 「最低一回は開店する」ので「1度も開店してない」状態以外についてのみ考える
      temp_point = 0
      @n.times do |i|
        match_count = 0
        (0...10).each do |j|
          match_count += arr[j] == @shop_opens[i][j] && arr[j] == 1 ? 1 : 0
        end
        temp_point += @shop_points[i][match_count]
      end
      @ans = [@ans, temp_point].max
    end
  else
    # 探索
    nex_arr = arr.dup
    nex_arr[idx] = 1
    rec(nex_arr, idx+1)
    nex_arr[idx] = 0
    rec(nex_arr, idx+1)
  end
end

rec(time_period, 0)

puts @ans