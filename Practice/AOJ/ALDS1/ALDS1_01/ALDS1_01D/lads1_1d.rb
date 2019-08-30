n = gets.to_i
maxv, minv = -1e9, gets.to_i
(n-1).times do
    rj = gets.to_i
    maxv = [maxv, rj-minv].max
    minv = [minv, rj].min
    # puts "rj: #{rj}, maxv: #{maxv}, minv: #{minv}"
end

puts maxv