# これは自力で解いたケース
# 解答が出力されるまでにかなり時間がかかるダメ解答（2秒くらい？）
# 解答はあってるんだけどいちいちstrしたりと頭が悪い 悪すぎる

pi = 3.14159265358


def f(x):
    dominator, enumator = 1, 1
    while True:
        # 「小数第n位までで四捨五入」とかいう日本語だと+2になるわ
        t = round(enumator / (dominator * 1.0), x + 2)
        t = str(t)[:-2]
        if t == str(pi)[: 2 + x]:
            break
        if enumator / (1.0 * dominator) < pi:
            enumator += 1
        else:
            dominator += 1
        # print(
        #     "now result: enunator / dominator = {enu}/{dom} = {result}".format(
        #         enu=enumator, dom=dominator, result=enumator / (1.0 * dominator)
        #     )
        # )

    print(
        "{enu} / {dom} = {result}".format(
            enu=enumator, dom=dominator, result=enumator / dominator
        )
    )


f(11)
