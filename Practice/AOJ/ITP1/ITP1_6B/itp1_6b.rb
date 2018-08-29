n = gets.to_i
suits = ["S", "H", "C", "D"]
# rubyで２次元配列初期化するときこんな感じ
cards = Array.new(suits.size).map { Array.new((1..13).to_a) }
n.times do
    # pythonでいうところのisnumericで分ける的なやつ pythonと違って漢数字とかには使えないけど
    # suit, score = gets.chomp.split.map { |s| s=~ /^\d$/ ? s.to_i : s }
    suit, score = gets.chomp.split.map { |s| s.match?(/^\d+$/) ? s.to_i : s }
    # puts "suit: #{suit} score: #{score}"
    if cards[suits.index(suit)].include?(score)
        cards[suits.index(suit)].delete(score)
        # print cards
        # puts
    end
end

cards.each_with_index do |s, idx|
    s.each do |num|
        puts "#{suits[idx]} #{num}"
    end
end