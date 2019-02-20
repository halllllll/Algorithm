# ""と"*"または"*"と"*"または"*"と""で囲まれた部分に0が含まれてなければ1つを0に
# ""と"+"または"+"と"+"または"+"と""で囲まれた部分のうち0でないものを0に

s = gets.chomp.split("+")
c = 0
s.each do |t|
  if t.length>1 && !(t.include?('0'))
    c+=1
  elsif t.length==1 && t!="0"
    c+=1
  end
end
p c