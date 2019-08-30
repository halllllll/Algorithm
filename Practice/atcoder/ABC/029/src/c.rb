# 再帰が使えるかどうかの確認問題みたいなもん、Aレベル 

N = gets.to_i

def func(s)
  if s.length == N
    puts s
  else
    func(s+"a")
    func(s+"b")
    func(s+"c")
  end
end

func("a")
func("b")
func("c")