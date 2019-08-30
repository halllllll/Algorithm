# frozen_string_literal: true

# Primeモジュールは使わない縛り
n = gets.to_i
prime_list = [] # すでに発見済みの素数を記録しておく

def is_prime(v)
  # 平方根の計算
  x = v**0.5
  # 判定処理
  (2..x.to_i).each do |i|
    return false if (v % i).zero?
  end
  true
end

n.times do
  x = gets.to_i
  prime_list << x if !prime_list.include?(x) && is_prime(x)
end
puts prime_list.size
