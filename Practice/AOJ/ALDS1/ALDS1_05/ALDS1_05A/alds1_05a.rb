$n = gets.chomp.to_i
$a = gets.chomp.split.map(&:to_i)
q = gets.chomp.to_i
m = gets.chomp.split.map(&:to_i)

# 各要素について採用するかしないかの2択
$table = []
def func(now, depth)
  if depth == $n
    $table << now
  else
    func(now + $a[depth], depth+1)
    func(now, depth+1)
  end
end

# すべての組み合わせを探索して配列に置いておく
func(0, 0)

m.each do |mm|
  puts $table.include?(mm) ? 'yes' : 'no'
end
