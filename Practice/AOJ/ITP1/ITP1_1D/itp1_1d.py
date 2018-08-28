S = int(input())
h, m, s = S//(60*60), S % 3600//60, S % 60
print("{h}:{m}:{s}".format(h=h, m=m, s=s))
