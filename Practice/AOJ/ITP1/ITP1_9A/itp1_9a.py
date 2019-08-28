s = input()
c = 0
while True:
    words = input()
    if words == "END_OF_TEXT":
        break
    # words = list(map(upper, words.split())
    wordcount = list(filter(lambda word: word.upper()
                            == s.upper(), words.split()))
    # print("{}".format(wordcount))
    c += len(wordcount)
print(c)
