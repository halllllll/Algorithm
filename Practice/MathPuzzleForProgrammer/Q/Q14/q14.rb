countory = ["Brazil", "Croatia", "Mexico", "Cameroon", "Spain", "Netherlandss", "Chille", "Australia", "Colombia", "Greece", "Cote d'lvoire", "Japan", "Uruguay", "Costa Rica", "England", "Italy", "Switzerland", "Ecuador", "France", "Honduras", "Argentina", "Bosnia and Herzegovina", "Iran", "Nigeria", "Germany", "Portugal", "Ghana", "USA", "Belgium", "Algeria", "Rossia", "Korea Republic"]
countory = countory.map(&:upcase)
@max = 0
@find_max = [[]]

def dfs(now, zan)
  zan.each do |z|
    dfs(now.clone << z, zan - [z]) if now[-1][-1] == z[0]
  end
  if @max <= now.size
    @max = now.size
    @find_max = @find_max.select{|f| f.size >= @max} << now
  end
end

countory.each do |c|
  dfs([c], countory - [c])
end

p @max
@find_max.each do |f|
  p f.join(" -> ")
end