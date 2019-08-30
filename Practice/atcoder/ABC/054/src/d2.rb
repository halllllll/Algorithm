# ナップザック
N, A, B = gets.chomp.split.map(&:to_i)
@a_arr, @b_arr, @c_arr = [], [], []
N.times do
    a, b, c = gets.chomp.split.map(&:to_i)
    @a_arr << a; @b_arr << b; @c_arr << c
end
@memo = Array.new(N).map{Array.new(40*10+1).map{Array.new(40*10+1, -1)}}
def rec(i, a, b, c)
    # 見つかった場合は終了
    if a*b>0 && a*B == A*b
        return c
    end
    # 探索できなかったら終了
    if i==N
        return 10**10
    end
    # 既に探索済みならそれを返す
    if @memo[i][a][b] > 0
        return @memo[i][a][b]
    end
    ret = [rec(i+1, a+@a_arr[i], b+@b_arr[i], c+@c_arr[i]), rec(i+1, a, b, c)].min
    @memo[i][a][b] = ret
    return ret
end

ans = rec(0, 0, 0, 0)
puts ans==10**10 ? -1 : ans