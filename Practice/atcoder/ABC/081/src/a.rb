# puts gets.chomp.chars.map(&:to_i).sum atcoderで使ってるrubyのバージョンではsumが使えない
puts gets.chomp.chars.map(&:to_i).inject(:+)