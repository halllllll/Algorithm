word = gets.chomp
c = 0
# この書き方でもEOFなるまで一行ずつとれる
STDIN.each_line {|line|
    c += line.chomp.downcase.split.count word.downcase
}
puts c
