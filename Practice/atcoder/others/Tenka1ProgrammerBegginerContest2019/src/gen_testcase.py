from random import randint
from os import path
x = 2 * 10**5
print("length: {}".format(x))
with open(path.dirname(__file__) + "/testcase.txt", mode="w",
          encoding="utf-8") as f:
    f.write(str(x))
    f.write("\n")
    for _ in range(x):
        a = ["#", "."][randint(0, 1)]
        f.write(a)
    f.write("\n")
print("done..........")