n, k = map(int, input().split())
w = [int(input()) for n in range(n)]


def f(w, max_n):
    right = max_n
    left = max(w)
    while True:
        mid = int((right+left)/2)
        # print("l: {} r: {} mid: {}".format(left, right, mid))
        if right - left < 1:
            return mid

        amount = 0
        count = 1
        for wi in w:
            if amount+wi > mid:
                count += 1
                amount = wi
            else:
                amount += wi
        if count > k:
            # 今のmだと🚙の台数が足りない
            left = mid + 1
        else:
            # 今のmで🚗の台数が足りる
            right = mid


print(f(w, 10000000000000))
