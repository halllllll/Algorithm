# y,x=0,0からスタートする

def trace(path)
  return 1 if path.size == N+1
  ret = 0 # *1
  now = path.last
  step = [0, -1, 0, 1, 0]
  for i in (0..3) do
    next_y = step[i] + now[0]
    next_x = step[i+1] + now[1]
    next_step = [next_y, next_x]
    if !path.include?(next_step)
      next_path = path.clone
      next_path << next_step
      ret += trace(next_path)
    end
  end
  ret # *3
end

start = [0, 0]
pathisited = [start]
N = 4
puts trace(pathisited)  # 0オーダーだったので

# *1 *2 *3が実装できなかった....
# arrayの << と + では 追加 と 連結 の違いがあるらしい