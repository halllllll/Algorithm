# うまいことやる せいぜいopは2^3なので愚直にやってもいいけど
# evalを使ってもいいけどevilなので使わない方針

a, b, c, d = list(map(int, list(input())))
op1, op2, op3 = [True, False], [True, False], [True, False]
for o1 in op1:
    for o2 in op2:
        for o3 in op3:
            ab = a + b if o1 else a - b
            abc = ab + c if o2 else ab - c
            abcd = abc + d if o3 else abc - d
            if abcd == 7:
                opr1 = "+" if o1 else "-"
                opr2 = "+" if o2 else "-"
                opr3 = "+" if o3 else "-"
                print("{}{}{}{}{}{}{}=7".format(a, opr1, b, opr2, c, opr3, d))
                exit()
