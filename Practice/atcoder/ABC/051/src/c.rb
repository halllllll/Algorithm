sx, sy, tx, ty = gets.chomp.split.map(&:to_i)
print "U"*(ty-sy).abs+"R"*(tx-sx).abs
print "U"+"L"*((tx-sx).abs+1)+"D"*((ty-sy).abs+1)+"R"
print "R"*(tx-sx).abs+"U"*(ty-sy).abs
print "R"+"D"*((ty-sy).abs+1)+"L"*((tx-sx).abs+1)+"U"
puts