a, b = map(int, input().split())
# a/bだとeやらEやら（名称忘れた）も出力されてしまうので小数点以下をフォーマットした
print(a//b, a % b, format(a/b, '.10f'))
