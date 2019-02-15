n, k = gets.chomp.split.map(&:to_i)
puts (n/2.0).ceil < k ? "NO" : "YES"