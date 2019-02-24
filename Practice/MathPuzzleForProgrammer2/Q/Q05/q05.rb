# 段での合計をgrudyするのではなく、段の各値をgrudyするので配列でもっておく
# n段目の個数はn+1なのでn+1の配列をもって0で初期化しておき、
# 次の段に進むごとに「i=1からスタートして[i]+[i+1]して頭と尻は1」
# （尻から計算するとひとつの配列で済むけどめんどくさいので都度コピーすることにした）
arr = Array.new(46, 0)
arr[0], arr[1] = 1, 1

n = 2
while n<=45 do
  temp_arr = arr.clone
  (1..n).to_a.each do |i|
    arr[i] = temp_arr[i]+temp_arr[i-1]
  end
  arr[n] = 1
  n+=1
end
# grudy
ans = 0
money = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
arr.each do |ai|
  money.each do |mi|
    ans += ai/mi
    ai %= mi
  end
end
puts ans
