# sはありったけ使うほうがいい（cから作るとコストがかかる）
# ありったけ = m//2
# 残ったcからsccを作るには4つ必要

n, m = map(int, input().split())
c = min(n, m // 2)
c += max(0, (m-2*n) // 4)
print(c)
