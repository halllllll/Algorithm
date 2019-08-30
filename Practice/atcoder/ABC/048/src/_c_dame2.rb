# どうしてもdpっぽいから再チャレンジ
# いけたっぽいけどなんか納得感よりも泥臭い疲労感が...

N, X = gets.chomp.split.map(&:to_i)
kubikari = 0
L = gets.chomp.split.map(&:to_i).map do |l|
  if l>X
    kubikari += l-X
    X
  else
    l
  end
end
L << 0  # うーん....

p L, kubikari
INF = 10**9
@memo = Array.new(N+1).map{Array.new(10, nil)}


# これもabc011?のcで失敗したときと同じで、このやり方だと「既に通ったところ」はそのときの値を返してしまっている...
# なので、既にあるときにsと比べて探索を変えてみる
def rec(i, a, b, s, l)
  if i==N-1
    # puts "#{l}(#{s})"
    return s
  else
    if (a+b)<=X
      return rec(i+1, b, L[i+2], s, l)
    elsif @memo[i][a].nil?.! && @memo[i][a] <= s
      return @memo[i][a]
    else
      ret = INF
      afure = (a+b)-X
      0.upto(afure).each do |j|
        nex_a = a-(afure-j)
        nex_b = b-j
        # puts "-"*i + "#{i}番目を#{nex_a}, #{i+1}番目を#{nex_b}にした"
        tes_l = l.clone
        tes_l[i], tes_l[i+1] = nex_a, nex_b
        # puts "-"*i+"#{tes_l}"
        ret = [ret, rec(i+1, nex_b, L[i+2], s+afure, tes_l)].min
        @memo[i][nex_a] = ret
      end
      return ret
    end
  end
end


p rec(0, L[0], L[1], 0, L.clone)+kubikari