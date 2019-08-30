# frozen_string_literal: true

# だるいので全探索
dishes = 5.times.map { gets.chomp.to_i }

ans = 10**9
arr = (0..4).to_a.permutation.to_a
arr.each do |a|
  t = 0
  a.each.with_index do |vi, idx|
    t += if idx < 4
           if dishes[vi] % 10 != 0
             (dishes[vi] + (10 - dishes[vi] % 10))
           else
             dishes[vi]
           end
         else
           dishes[vi]
         end
  end
  ans = [ans, t].min
end

puts ans
