N = 12


def func(path):
    if(len(path) == N + 1):
        return 1
    cur = path[-1]
    step = [0, -1, 0, 1, 0]
    ret = 0
    for i in range(4):
        n_y = cur[0] + step[i]
        n_x = cur[1] + step[i+1]
        next_step = [n_y, n_x]
        if next_step not in path:
            next_path = path[:]
            next_path.append(next_step)
            ret += func(next_path)
    return ret


print(func([[0, 0]]))
