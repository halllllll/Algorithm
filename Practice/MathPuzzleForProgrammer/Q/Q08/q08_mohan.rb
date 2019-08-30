N = 12

def move1(log)
  return 1 if log.size == N+1
  ret = 0
  step = [[0, 1], [-1, 0], [0, -1], [1, 0]]
  step.each do |s|
    nex = [log[-1][0]+s[0], log[-1][1]+s[1]]
    if !log.include?(nex)
      ret += move1(log+[nex])
    end
  end
  ret
end

def move(log)
  # return 1 if log.size == N+1
  if log.size == N+1
    # puts "成功"
    return 1
  end

  ret = 0
  [[0, 1], [0, -1], [1, 0], [-1, 0]].each do |d|
    nex = [log[-1][0] + d[0], log[-1][1] + d[1]]
    if !log.include?(nex)
      ret += move(log + [nex])
    end
  end
  ret
end

puts move1([[0, 0]])