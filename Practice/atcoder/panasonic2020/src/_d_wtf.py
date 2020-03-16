# なんでこれでだめなの
n = int(input())
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def dfs(s):
    if len(s) == n:
        print(s)
    else:
        pre = "a"
        idx = 0
        for i, c in enumerate(list(s)[:-1]):
            if pre < c:
                pre = c
                idx = i
        for i in range(idx + 2):
            dfs(s + alphabets[i])


dfs("a")