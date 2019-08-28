# 逆ポーランド記法ってスタックが話題になるときだけイキりだすよな...
arr = gets.chomp.split.map{|x| x.match(/\d/) ? x.to_i : x}
# evalは使わない

stack = []
arr.each do |item|
  if item.is_a?(Integer)
    stack << item
  else
    nx = case item
      when '+'
        stack.pop(2).inject(&:+)
      when '-'
        stack.pop(2).inject(&:-)
      when '*'
        stack.pop(2).inject(&:*)
      end
    stack << nx
  end
end
puts stack.pop