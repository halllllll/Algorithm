## 問題名
Print a Frame
## キーワード
?
## 概要
二数*H W*が与えられる。横*W*個・縦*H*個の**枠**を出力する。**枠**とは、W*Hの領域の最も外側の部分を`#`、それ以外の部分を`.`で表すことを示す。`0 0`が入力されるまで続ける。それぞれの（入力に対する）出力ごとに１行空ける。
## 方針と読解
最初と最後は`#`*Wであとは`.`を`#`でサンドしたらいいんじゃない
## 参考
とくになし
## 所感
rubyでやってるとき最初
```ruby
loop do
    h, w = gets.chomp.split.map(&:to_i)
    break if (h + w).zero?

    line = '#' * w
    for y in (0...h) do
        # puts "y: #{y}"
        line = y.between?(1, h) ? '#' + '.' * (w - 2) + '#' : line
        puts line
    end
    puts
end
 
```
としたらなぜか各入力の最終出力行が思うようにいかなかった。これで1時間くらいハマっていたきがする。

結局解決できず、別の書き方をしたら通った。
```ruby
loop do 
    h, w = gets.chomp.split.map(&:to_i)
    if (h + w).zero?
        break
    end
    (0...h).each do |i|
        if i.between?(1, h - 2)
            puts '#' + '.' * (w - 2) + '#'
        else
            puts '#' * w
        end
    end
    puts
end
```