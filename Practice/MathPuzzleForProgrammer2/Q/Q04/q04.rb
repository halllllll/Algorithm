# 時間はループで網羅できるのと、数値と点灯する数をテーブルしておけばあとはカウントするだけ
# カウントは1桁の場合をちゃんとみるだけ
table = {0 => 6, 1 => 2, 2 => 5, 3 => 5, 4 => 4, 5 => 5, 6 => 6, 7 => 3, 8 => 7, 9 => 6}
ans = 0
0.upto(23).each do |h|
  h_d, h_m = h.divmod(10)
  0.upto(59).each do |m|
    m_d, m_m = m.divmod(10)
    0.upto(59).each do |s|
      s_d, s_m = s.divmod(10)
      count = table[h_d] + table[h_m] + table[m_d] + table[m_m] + table[s_d] + table[s_m]
      if count == 30
        ans += 1
      end
    end
  end
end

puts ans