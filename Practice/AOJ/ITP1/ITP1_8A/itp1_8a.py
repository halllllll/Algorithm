# クレバーだけどなんか強引なバージョン

from string import ascii_lowercase, ascii_uppercase
s = input()
table = str.maketrans(dict(zip(ascii_lowercase+ascii_uppercase,
                               ascii_uppercase+ascii_lowercase)))
print(s.translate(table))
