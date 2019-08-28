桁DPの典型は、整数nが与えられたとき、0~nまでの中で条件を満たす数を数え上げるというもの。

よくある条件は
- 特定の数字が含まれる
- 各桁の数の和がxである

など。

上位の桁から探索していき、**「上位からi桁目」** と **「その時までに条件を満たしているかどうかのbool」** という状態をもたせるのが基本。条件によって更にここにもたせる情報を追加していく流れ

たとえば超基本中の基本で、<u>*N以下の数値はいくつあるか*</u>という問題だと以下のような感じの再帰になり、あとはメモ化してやればいい。

```python
n = "4837"

def rec(i, boolean):
    if i == len(n):
        return 1
    else:
        ret = 0
        limit = int(n[i]) if boolean is True else 9
        for j in range(limit + 1):
            nex_boolean = j <= limit and boolean is True
            ret += rec_non_memo(i+1, nex_boolean)
        return ret


print(rec(0, True))

```